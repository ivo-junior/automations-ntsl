import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from datetime import datetime, time
import warnings

from .ntsl_parser import NTSLStrategy
from .technical_indicators import TechnicalIndicators

@dataclass
class Trade:
    """Representa uma operação completa"""
    entry_time: datetime
    exit_time: Optional[datetime]
    direction: str  # 'LONG' ou 'SHORT'
    entry_price: float
    exit_price: Optional[float]
    quantity: int
    result: Optional[float]
    status: str  # 'OPEN', 'CLOSED', 'STOPPED'
    stop_loss: Optional[float] = None
    take_profit: Optional[float] = None

@dataclass
class BacktestResult:
    """Resultado completo do backtest"""
    trades: List[Trade]
    equity_curve: pd.Series
    metrics: Dict[str, float]
    strategy_name: str
    asset: str
    timeframe: str
    period: str
    total_bars: int

class BacktestEngine:
    """
    Engine principal para execução de backtest de estratégias NTSL
    Baseado na documentação em docs/ e exemplos do catalog.md
    """
    
    def __init__(self):
        self.data: pd.DataFrame = None
        self.strategy: NTSLStrategy = None
        self.trades: List[Trade] = []
        self.current_position = 0
        self.current_trade: Optional[Trade] = None
        self.equity = []
        self.daily_results = {}
        self.indicators = TechnicalIndicators()
        
        # Estado da estratégia baseado em padrões do catálogo
        self.strategy_state = {
            'ultimoDia': None,
            'tradesHoje': 0,
            'lossConsecutivo': 0,
            'resultadoDiario': 0.0,
            'posicaoAberta': False,
            'bloqueadoMeta': False,
            'bloqueadoLossConsec': False,
            'primeiraBarraDefinida': False,
            'maximaPrimeiraBarra': 0.0,
            'minimaPrimeiraBarra': 999999.0
        }
        
    def run_backtest(self, strategy: NTSLStrategy, data: pd.DataFrame, asset: str, timeframe: str) -> BacktestResult:
        """Executa backtest completo"""
        self.strategy = strategy
        self.data = data.copy()
        self._prepare_data()
        self._initialize_strategy_variables()
        
        print(f"Iniciando backtest da estratégia: {strategy.name}")
        print(f"Ativo: {asset} | Tempo Gráfico: {timeframe}")
        print(f"Período: {data.index[0].date()} a {data.index[-1].date()}")
        print(f"Total de barras: {len(data)}")
        
        # Executar barra por barra
        for i in range(len(self.data)):
            self.current_bar = i
            self._execute_bar(i)
        
        # Fechar posição aberta ao final
        if self.current_position != 0:
            self._close_position(len(self.data) - 1, "END_OF_DATA")
        
        # Calcular métricas
        metrics = self._calculate_metrics()
        
        return BacktestResult(
            trades=self.trades.copy(),
            equity_curve=pd.Series(self.equity, index=self.data.index),
            metrics=metrics,
            strategy_name=strategy.name,
            asset=asset,
            timeframe=timeframe,
            period=f"{data.index[0].date()}_a_{data.index[-1].date()}",
            total_bars=len(data)
        )
    
    def _prepare_data(self):
        """Prepara dados com indicadores baseados na documentação NTSL"""
        # Garantir colunas OHLCV
        required_cols = ['open', 'high', 'low', 'close', 'volume']
        for col in required_cols:
            if col not in self.data.columns:
                raise ValueError(f"Coluna obrigatória '{col}' não encontrada nos dados")
        
        # Calcular indicadores baseados nos parâmetros da estratégia
        # Médias Móveis (conforme docs/funcoes_constantes_NTSL.md)
        if 'lw_mediaTendencia' in self.strategy.inputs:
            periodo = int(self.strategy.inputs['lw_mediaTendencia'])
            # Voltando para SMA, para isolar o efeito da mudança nas Bollinger Bands
            self.data['media_tendencia'] = self.indicators.sma(self.data['close'], periodo)
            
        if 'lw_mediaSinal' in self.strategy.inputs:
            periodo = int(self.strategy.inputs['lw_mediaSinal'])
            # Média do sinal continua como SMA, conforme setup clássico
            self.data['media_sinal_high'] = self.indicators.sma(self.data['high'], periodo)
            self.data['media_sinal_low'] = self.indicators.sma(self.data['low'], periodo)
            
        # Bollinger Bands (baseado nos exemplos do catálogo)
        if 'bb_periodo' in self.strategy.inputs:
            periodo = int(self.strategy.inputs['bb_periodo'])
            desvio = float(self.strategy.inputs.get('bb_desvio', 2.0))
            tipo_media_int = int(self.strategy.inputs.get('bb_tipoMedia', 0))

            # Mapear o inteiro do NTSL para o tipo de média
            ma_type_map = {0: 'sma', 1: 'ema', 2: 'smma', 3: 'lwma'}
            ma_type = ma_type_map.get(tipo_media_int, 'sma')
            
            bb_upper, bb_middle, bb_lower = self.indicators.bollinger_bands(
                self.data['close'], periodo, desvio, ma_type=ma_type)
            self.data['bb_upper'] = bb_upper
            self.data['bb_middle'] = bb_middle  
            self.data['bb_lower'] = bb_lower
            
        # ATR para gestão de risco (padrão em muitas estratégias do catálogo)
        if 'filtro_volatilidade_atrPeriodo' in self.strategy.inputs:
            periodo = int(self.strategy.inputs['filtro_volatilidade_atrPeriodo'])
            self.data['atr'] = self.indicators.atr(self.data, periodo)
    
    def _initialize_strategy_variables(self):
        """Inicializa variáveis de estado da estratégia"""
        self.strategy_vars = self.strategy.variables.copy()
        self.strategy_vars.update({
            'ultimoDia': None,
            'tradesHoje': 0,
            'lossConsecutivo': 0,
            'resultadoDiario': 0.0,
            'posicaoAberta': False,
            'bloqueadoMeta': False,
            'bloqueadoLossConsec': False
        })
        
        self.current_position = 0
        self.trades = []
        self.equity = []
        self.current_trade = None
    
    def _calculate_larry_williams_signal(self, bar_idx: int) -> int:
        """
        Implementa Setup Larry Williams conforme STP0003 do catálogo
        Baseado no exemplo: STP0003_Trade_e_Acoes_Setup_Larry_Williams_Classico
        """
        if bar_idx < 20:  # Precisa de dados suficientes
            return 0
            
        try:
            current_data = self.data.iloc[bar_idx]
            
            # Conforme STP0003: usa média da tendência e médias dos sinais
            tendencia = current_data.get('media_tendencia')
            media_sinal_low = current_data.get('media_sinal_low')  
            media_sinal_high = current_data.get('media_sinal_high')
            
            if pd.isna(tendencia) or pd.isna(media_sinal_low) or pd.isna(media_sinal_high):
                return 0
                
            close = current_data['close']
            low = current_data['low']
            high = current_data['high']
            
            # Sinal de compra: Close > tendência E Low < média do sinal (Low)
            if close > tendencia and low < media_sinal_low:
                return 1
            # Sinal de venda: Close < tendência E High > média do sinal (High)  
            elif close < tendencia and high > media_sinal_high:
                return -1
            else:
                return 0
                
        except (KeyError, IndexError):
            return 0
    
    def _calculate_primeira_barra_signal(self, bar_idx: int) -> int:
        """
        Implementa Setup Primeira Barra conforme V0045 do catálogo
        Baseado no exemplo: V0045_Setup_Primeira_Barra
        """
        try:
            current_data = self.data.iloc[bar_idx]
            current_time = current_data.name.time()
            
            # Definir primeira barra (ex: 09:00 às 09:15)
            start_time = self.strategy.inputs.get('pb_horaInicio', 900)  # 09:00
            end_time = self.strategy.inputs.get('pb_horaFim', 915)      # 09:15
            
            # Converter para time objects
            start_hour, start_min = divmod(start_time, 100)
            end_hour, end_min = divmod(end_time, 100)
            
            # Se estamos no período de definição da primeira barra
            if (current_time.hour == start_hour and current_time.minute >= start_min) or \
               (current_time.hour == end_hour and current_time.minute <= end_min):
                # Atualizar máximas e mínimas
                if current_data['high'] > self.strategy_state['maximaPrimeiraBarra']:
                    self.strategy_state['maximaPrimeiraBarra'] = current_data['high']
                if current_data['low'] < self.strategy_state['minimaPrimeiraBarra']:
                    self.strategy_state['minimaPrimeiraBarra'] = current_data['low']
                return 0
            
            # Após o período, verificar rompimentos
            if current_time.hour > end_hour or \
               (current_time.hour == end_hour and current_time.minute > end_min):
                
                if not self.strategy_state['primeiraBarraDefinida']:
                    self.strategy_state['primeiraBarraDefinida'] = True
                
                # Verificar rompimento da máxima
                if (current_data['high'] > self.strategy_state['maximaPrimeiraBarra'] and 
                    self.data.iloc[bar_idx-1]['high'] <= self.strategy_state['maximaPrimeiraBarra']):
                    return 1
                    
                # Verificar rompimento da mínima  
                elif (current_data['low'] < self.strategy_state['minimaPrimeiraBarra'] and
                      self.data.iloc[bar_idx-1]['low'] >= self.strategy_state['minimaPrimeiraBarra']):
                    return -1
            
            return 0
            
        except (KeyError, IndexError):
            return 0
    
    def _calculate_bollinger_signal(self, bar_idx: int) -> int:
        """
        Implementa Bollinger Breakout conforme BollingerBreakout do catálogo
        """
        try:
            current_data = self.data.iloc[bar_idx]
            close = current_data['close']
            bb_upper = current_data.get('bb_upper')
            bb_lower = current_data.get('bb_lower')
            
            if pd.isna(bb_upper) or pd.isna(bb_lower):
                return 0
            
            # Rompimento das bandas (estratégia de breakout)
            if close > bb_upper:
                return 1
            elif close < bb_lower:
                return -1
            else:
                return 0
                
        except (KeyError, IndexError):
            return 0
    
    def _execute_bar(self, bar_idx: int):
        """Executa a lógica da estratégia para uma barra, garantindo que o equity seja sempre registrado."""
        current_data = self.data.iloc[bar_idx]

        # 1. Atualizar controles diários
        self._update_daily_controls(current_data)

        # 2. Checar condições de encerramento ou de trade
        hora_encerramento = self.strategy.inputs.get('horaEncerramento', 1750)
        is_after_close_time = (current_data.name.hour * 100 + current_data.name.minute) >= hora_encerramento

        if self.current_position != 0:
            # Se tem posição, ou encerra por tempo, ou checa stops/gains
            if is_after_close_time:
                self._close_position(bar_idx, "END_OF_SESSION")
            else:
                self._check_exit_conditions(bar_idx, current_data)
        elif not is_after_close_time:
            # Se não tem posição e não é fim do dia, checa por entradas
            self._check_entry_conditions(bar_idx, current_data)

        # 3. Calcular e registrar o equity no final da barra, independentemente do que aconteceu
        current_equity = self._calculate_current_equity(current_data)
        self.equity.append(current_equity)
    
    def _update_daily_controls(self, current_data):
        """Atualiza controles diários de risco"""
        current_date = current_data.name.date()
        
        if self.strategy_state['ultimoDia'] != current_date:
            self.strategy_state['ultimoDia'] = current_date
            self.strategy_state['tradesHoje'] = 0
            self.strategy_state['resultadoDiario'] = 0.0
            self.strategy_state['bloqueadoMeta'] = False
            
        # Verificar limites diários
        lucro_max = self.strategy.risk_params.get('lucroMaximoDiario', 0)
        risco_max = self.strategy.risk_params.get('riscoMaximoDiario', 0)
        
        if lucro_max > 0 and self.strategy_state['resultadoDiario'] >= lucro_max:
            self.strategy_state['bloqueadoMeta'] = True
            
        if risco_max > 0 and self.strategy_state['resultadoDiario'] <= -risco_max:
            self.strategy_state['bloqueadoMeta'] = True
    
    def _check_entry_conditions(self, bar_idx: int, current_data):
        """Verifica condições de entrada baseadas no orquestrador moderado"""
        # Atualizar estado de bloqueio por loss consecutivo
        max_loss_consec = self.strategy.risk_params.get('maxLossConsecutivo', 999)
        if self.strategy_state['lossConsecutivo'] >= max_loss_consec:
            self.strategy_state['bloqueadoLossConsec'] = True

        # Verificar bloqueios
        if (self.strategy_state['bloqueadoMeta'] or 
            self.strategy_state['bloqueadoLossConsec']):
            return
            
        max_trades = self.strategy.risk_params.get('maxTradesPorDia', 999)
        if self.strategy_state['tradesHoje'] >= max_trades:
            return
        
        # Verificar janela horária
        usar_janela = self.strategy.inputs.get('usarJanelaHoraria', True)
        if usar_janela:
            hora_atual = current_data.name.time()
            inicio = self.strategy.inputs.get('horaInicioGlobal', 905)
            fim = self.strategy.inputs.get('horaFimGlobal', 1745)
            
            hora_inicio = f"{inicio//100:02d}:{inicio%100:02d}"
            hora_fim = f"{fim//100:02d}:{fim%100:02d}"
            
            # Verificar se está dentro da janela
            # (implementação simplificada - pode ser refinada)
            
        # Calcular sinais das estratégias internas  
        sinal_lw = self._calculate_larry_williams_signal(bar_idx)
        sinal_pb = self._calculate_primeira_barra_signal(bar_idx)
        sinal_bb = self._calculate_bollinger_signal(bar_idx)
        
        # Sistema de pontuação (orquestrador)
        peso_lw = float(self.strategy.inputs.get('peso_LarryWilliams', 0.4))
        peso_pb = float(self.strategy.inputs.get('peso_PrimeiraBarra', 0.3))
        peso_bb = float(self.strategy.inputs.get('peso_Bollinger', 0.3))
        
        score_compra = 0
        score_venda = 0
        
        if sinal_lw == 1:
            score_compra += peso_lw
        elif sinal_lw == -1:
            score_venda += peso_lw
            
        if sinal_pb == 1:
            score_compra += peso_pb
        elif sinal_pb == -1:
            score_venda += peso_pb
            
        if sinal_bb == 1:
            score_compra += peso_bb
        elif sinal_bb == -1:
            score_venda += peso_bb
        
        score_minimo = float(self.strategy.inputs.get('scoreMinimoEntrada', 0.5))
        
        # Executar entrada
        if score_compra >= score_minimo and score_compra > score_venda:
            self._open_position(bar_idx, 'LONG', current_data)
        elif score_venda >= score_minimo and score_venda > score_compra:
            self._open_position(bar_idx, 'SHORT', current_data)
    
    def _open_position(self, bar_idx: int, direction: str, current_data):
        """Abre nova posição e calcula stops/gains iniciais."""
        quantity = int(self.strategy.risk_params.get('contratosPorOperacao', 1))
        
        if direction == 'LONG':
            self.current_position = quantity
        else:
            self.current_position = -quantity
            
        # Calcular stops e gains com base no ATR do momento da entrada
        atr = current_data.get('atr', 0)
        if atr == 0: return # Evitar divisão por zero ou stops inválidos

        fator_stop = self.strategy.risk_params.get('fatorAtrStop', 2.0)
        fator_gain = self.strategy.risk_params.get('fatorAtrGain', 3.0)
        entry_price = current_data['close']

        stop_price = 0
        gain_price = 0

        if direction == 'LONG':
            if self.strategy.inputs.get('usarStopLoss', True):
                stop_price = entry_price - (atr * fator_stop)
            if self.strategy.inputs.get('usarStopGain', True):
                gain_price = entry_price + (atr * fator_gain)
        else: # SHORT
            if self.strategy.inputs.get('usarStopLoss', True):
                stop_price = entry_price + (atr * fator_stop)
            if self.strategy.inputs.get('usarStopGain', True):
                gain_price = entry_price - (atr * fator_gain)

        self.current_trade = Trade(
            entry_time=current_data.name,
            exit_time=None,
            direction=direction,
            entry_price=entry_price,
            exit_price=None,
            quantity=abs(quantity),
            result=None,
            status='OPEN',
            stop_loss=stop_price if stop_price > 0 else None,
            take_profit=gain_price if gain_price > 0 else None
        )
        
        self.strategy_state['posicaoAberta'] = True
        self.strategy_state['tradesHoje'] += 1
        
        print(f"Posição {direction} aberta em {current_data.name}: {entry_price:.2f}")
    
    def _check_exit_conditions(self, bar_idx: int, current_data):
        """Verifica todas as condições de saída: Stop, Gain, Breakeven, Trailing."""
        if self.current_trade is None or self.current_trade.status != 'OPEN':
            return

        trade = self.current_trade
        atr = current_data.get('atr', 0)
        if atr == 0: return

        # --- Lógica de Break Even ---
        if self.strategy.inputs.get('usarBreakEven', False) and trade.stop_loss < trade.entry_price:
            gatilho_be = self.strategy.inputs.get('gatilhoBreakevenAtr', 0.8)
            if current_data['high'] >= trade.entry_price + (atr * gatilho_be):
                trade.stop_loss = trade.entry_price # Mover stop para o breakeven

        # --- Lógica de Trailing Stop ---
        if self.strategy.inputs.get('usarTrailingStop', False):
            gatilho_ts = self.strategy.inputs.get('gatilhoTrailingAtr', 1.5)
            distancia_ts = self.strategy.inputs.get('distanciaTrailingAtr', 1.2)
            
            if trade.direction == 'LONG' and current_data['high'] >= trade.entry_price + (atr * gatilho_ts):
                novo_stop = current_data['close'] - (atr * distancia_ts)
                if novo_stop > trade.stop_loss:
                    trade.stop_loss = novo_stop # Trailing o stop
            elif trade.direction == 'SHORT' and current_data['low'] <= trade.entry_price - (atr * gatilho_ts):
                novo_stop = current_data['close'] + (atr * distancia_ts)
                if novo_stop < trade.stop_loss:
                    trade.stop_loss = novo_stop # Trailing o stop

        # --- Checagem final de Stops e Gains ---
        if trade.direction == 'LONG':
            # Checar Take Profit
            if trade.take_profit and current_data['high'] >= trade.take_profit:
                self._close_position(bar_idx, "TAKE_PROFIT", price=trade.take_profit)
                return
            # Checar Stop Loss
            if trade.stop_loss and current_data['low'] <= trade.stop_loss:
                self._close_position(bar_idx, "STOP_LOSS", price=trade.stop_loss)
        
        elif trade.direction == 'SHORT':
            # Checar Take Profit
            if trade.take_profit and current_data['low'] <= trade.take_profit:
                self._close_position(bar_idx, "TAKE_PROFIT", price=trade.take_profit)
                return
            # Checar Stop Loss
            if trade.stop_loss and current_data['high'] >= trade.stop_loss:
                self._close_position(bar_idx, "STOP_LOSS", price=trade.stop_loss)
    
    def _close_position(self, bar_idx: int, reason: str, price: Optional[float] = None):
        """Fecha posição atual, usando um preço específico se fornecido."""
        if self.current_trade is None:
            return
            
        current_data = self.data.iloc[bar_idx]
        # Usa o preço exato do stop/gain se fornecido, senão usa o fechamento da barra
        exit_price = price if price is not None else current_data['close']
        
        # Calcular resultado
        if self.current_trade.direction == 'LONG':
            result = (exit_price - self.current_trade.entry_price) * self.current_trade.quantity
        else:
            result = (self.current_trade.entry_price - exit_price) * self.current_trade.quantity
            
        # Converte o resultado em pontos para resultado financeiro
        pontos_por_tick = float(self.strategy.inputs.get('pontosPorTick', 1.0))
        result *= pontos_por_tick

        # Aplicar custos (o input é considerado o custo total da operação ida e volta)
        custo_operacao = float(self.strategy.inputs.get('custoPorContrato', 0))
        result -= custo_operacao
        
        # Atualizar trade
        self.current_trade.exit_time = current_data.name
        self.current_trade.exit_price = exit_price
        self.current_trade.result = result
        self.current_trade.status = 'CLOSED'
        
        self.trades.append(self.current_trade)
        
        # Atualizar controles
        self.strategy_state['resultadoDiario'] += result
        if result < 0:
            self.strategy_state['lossConsecutivo'] += 1
        else:
            self.strategy_state['lossConsecutivo'] = 0
            
        self.current_position = 0
        self.strategy_state['posicaoAberta'] = False
        self.current_trade = None
        
        print(f"Posição fechada em {current_data.name}: {exit_price} (Resultado: {result:.2f})")
    
    def _calculate_current_equity(self, current_data) -> float:
        """Calcula equity atual"""
        equity = sum(trade.result for trade in self.trades if trade.result is not None)
        
        # Adicionar resultado da posição aberta se houver
        if self.current_position != 0 and self.current_trade:
            if self.current_trade.direction == 'LONG':
                unrealized = (current_data['close'] - self.current_trade.entry_price) * self.current_trade.quantity
            else:
                unrealized = (self.current_trade.entry_price - current_data['close']) * self.current_trade.quantity
            equity += unrealized
            
        return equity
    
    def _calculate_metrics(self) -> Dict[str, float]:
        """Calcula métricas de performance"""
        if not self.trades:
            return {}
            
        results = [t.result for t in self.trades if t.result is not None]
        
        if not results:
            return {}
            
        winning_trades = [r for r in results if r > 0]
        losing_trades = [r for r in results if r < 0]
        
        total_trades = len(results)
        winning_count = len(winning_trades)
        losing_count = len(losing_trades)
        
        gross_profit = sum(winning_trades) if winning_trades else 0
        gross_loss = abs(sum(losing_trades)) if losing_trades else 0
        
        # O resultado líquido já tem os custos deduzidos de cada trade
        net_profit = sum(results)
        
        # Calcular custos totais
        custo_por_operacao = float(self.strategy.inputs.get('custoPorContrato', 0))
        total_costs = custo_por_operacao * total_trades

        win_rate = (winning_count / total_trades * 100) if total_trades > 0 else 0
        profit_factor = (gross_profit / gross_loss) if gross_loss > 0 else float('inf') if gross_profit > 0 else 0
        
        return {
            'net_profit': net_profit,
            'gross_profit': gross_profit, 
            'gross_loss': -gross_loss, # Mantido negativo para exibição
            'total_costs': total_costs,
            'profit_factor': profit_factor,
            'total_trades': total_trades,
            'winning_trades': winning_count,
            'losing_trades': losing_count,
            'win_rate': win_rate,
            'avg_trade': net_profit / total_trades if total_trades > 0 else 0,
            'avg_winner': sum(winning_trades) / len(winning_trades) if winning_trades else 0,
            'avg_loser': sum(losing_trades) / len(losing_trades) if losing_trades else 0
        }
