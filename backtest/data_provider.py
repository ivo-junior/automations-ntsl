import yfinance as yf
import pandas as pd
from typing import Optional, List
from datetime import datetime, timedelta
import warnings

class DataProvider:
    """
    Provedor de dados históricos para backtest
    """
    
    def __init__(self):
        self.supported_sources = ['yahoo', 'local_csv']
    
    def get_data(self, 
                 symbol: str, 
                 start_date: str, 
                 end_date: str, 
                 interval: str = '15m',
                 source: str = 'yahoo',
                 target_interval: Optional[str] = None) -> pd.DataFrame:
        """
        Obtém dados históricos
        
        Args:
            symbol: Símbolo do ativo (Yahoo) ou caminho do arquivo (CSV)
            start_date: Data início (formato 'YYYY-MM-DD')
            end_date: Data fim (formato 'YYYY-MM-DD')
            interval: Intervalo dos dados (para Yahoo Finance)
            source: Fonte dos dados ('yahoo', 'local_csv')
            target_interval: O tempo gráfico final para reamostragem (ex: '15min')
        """
        
        if source == 'yahoo':
            return self._get_yahoo_data(symbol, start_date, end_date, interval)
        elif source == 'local_csv':
            # O 'symbol' aqui é, na verdade, o caminho do arquivo
            return self._get_local_csv_data(symbol, start_date, end_date, target_interval)
        else:
            raise ValueError(f"Fonte não suportada: {source}")
    
    def get_available_symbols(self, market: str = 'BR') -> List[str]:
        """
        Retorna lista de símbolos disponíveis por mercado
        Baseado nos ativos mencionados no catálogo de estratégias
        """
        
        # Ativos brasileiros mencionados nas estratégias do catálogo
        symbols_br = [
            # Ações principais
            'PETR4.SA', 'VALE3.SA', 'ITUB4.SA', 'BBDC4.SA', 'ABEV3.SA',
            'B3SA3.SA', 'RENT3.SA', 'LREN3.SA', 'MGLU3.SA', 'VVAR3.SA',
            'WEGE3.SA', 'JBSS3.SA', 'SUZB3.SA', 'RAIL3.SA', 'CIEL3.SA',
            
            # Mini contratos (símbolos aproximados - ajustar conforme broker)
            'WINQ23.SA',  # Mini Índice Bovespa
            'WDOQ23.SA',  # Mini Dólar
            'INDQ23.SA',  # Índice Bovespa  
            'DOLQ23.SA',  # Dólar Futuro
            
            # ETFs
            'BOVA11.SA', 'SMAL11.SA', 'IVVB11.SA'
        ]
        
        symbols_us = [
            # Índices e ETFs principais
            'SPY', 'QQQ', 'IWM', 'DIA', 'VTI', 'EFA', 'EEM',
            
            # Ações de tecnologia  
            'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NVDA',
            
            # Outras ações importantes
            'BRK-B', 'JPM', 'JNJ', 'V', 'PG', 'UNH', 'HD', 'MA',
            
            # Commodities e outros
            'GLD', 'SLV', 'USO', 'TLT', 'HYG'
        ]
        
        # Criptomoedas (aproximação via Yahoo Finance)
        symbols_crypto = [
            'BTC-USD', 'ETH-USD', 'BNB-USD', 'ADA-USD', 'SOL-USD'
        ]
        
        if market.upper() == 'BR':
            return symbols_br
        elif market.upper() == 'US':
            return symbols_us
        elif market.upper() == 'CRYPTO':
            return symbols_crypto
        else:
            return symbols_br + symbols_us
    
    def validate_symbol(self, symbol: str) -> bool:
        """Valida se símbolo existe e tem dados disponíveis"""
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info
            return 'regularMarketPrice' in info or 'previousClose' in info
        except:
            return False
    
    def get_symbol_info(self, symbol: str) -> dict:
        """Obtém informações básicas do símbolo"""
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info
            
            return {
                'name': info.get('longName', symbol),
                'currency': info.get('currency', 'USD'),
                'exchange': info.get('exchange', 'N/A'),
                'sector': info.get('sector', 'N/A'),
                'market_cap': info.get('marketCap', 0),
                'price': info.get('regularMarketPrice', info.get('previousClose', 0))
            }
        except:
            return {'name': symbol, 'currency': 'USD', 'exchange': 'N/A'}
    
    def _get_yahoo_data(self, symbol: str, start_date: str, end_date: str, interval: str) -> pd.DataFrame:
        """Obtém dados do Yahoo Finance com tratamento para ativos brasileiros"""
        
        # Mapear intervalos para formato yfinance
        interval_map = {
            '1m': '1m', '2m': '2m', '5m': '5m', '15m': '15m', '30m': '30m',
            '60m': '1h', '1h': '1h', '1d': '1d', '5d': '5d', '1wk': '1wk', 
            '1mo': '1mo', '3mo': '3mo'
        }
        
        if interval not in interval_map:
            raise ValueError(f"Intervalo não suportado: {interval}. Disponíveis: {list(interval_map.keys())}")
        
        try:
            ticker = yf.Ticker(symbol)
            data = ticker.history(
                start=start_date,
                end=end_date,
                interval=interval_map[interval],
                auto_adjust=True,
                prepost=False,
                actions=False  # Não incluir dividendos/splits para simplificar
            )
            
            if data.empty:
                raise ValueError(f"Nenhum dado encontrado para {symbol} no período {start_date} a {end_date}")
            
            # Padronizar nomes das colunas para minúsculo
            data.columns = [col.lower().replace(' ', '_') for col in data.columns]
            
            # Garantir que temos as colunas necessárias
            required_cols = ['open', 'high', 'low', 'close', 'volume']
            missing_cols = [col for col in required_cols if col not in data.columns]
            
            if missing_cols:
                raise ValueError(f"Colunas obrigatórias não encontradas: {missing_cols}")
            
            # Remover dados com NaN
            data = data.dropna()
            
            if len(data) == 0:
                raise ValueError(f"Todos os dados contêm valores NaN para {symbol}")
            
            print(f"Dados obtidos: {len(data)} barras de {symbol} ({start_date} a {end_date})")
            print(f"   Intervalo: {interval} | Período: {data.index[0]} até {data.index[-1]}")
            
            return data[required_cols]
            
        except Exception as e:
            print(f"Erro ao obter dados do Yahoo Finance: {str(e)}")
            raise ValueError(f"Erro ao obter dados do Yahoo Finance para {symbol}: {str(e)}")
    
    def _get_local_csv_data(self, file_path: str, start_date: Optional[str], end_date: Optional[str], target_interval: Optional[str] = None) -> pd.DataFrame:
        """Carrega dados de arquivo CSV local e realiza reamostragem."""
        
        try:
            # Carregar dados do CSV com formato específico
            try:
                data = pd.read_csv(
                    file_path,
                    sep=';',
                    encoding='utf-8',
                    decimal=',',
                    thousands='.',
                    parse_dates=['Data'],
                    index_col='Data',
                    dayfirst=True
                )
            except UnicodeDecodeError:
                # Tentar latin-1 se utf-8 falhar
                data = pd.read_csv(
                    file_path,
                    sep=';',
                    encoding='latin-1',
                    decimal=',',
                    thousands='.',
                    parse_dates=['Data'],
                    index_col='Data',
                    dayfirst=True
                )
            
            # Mapeamento robusto de nomes de coluna
            # Lista de possíveis nomes para cada coluna padrão (case-insensitive e com/sem acentos)
            col_candidates = {
                'open': ['abertura', 'open'],
                'high': ['maxima', 'máxima', 'm_xima', 'high', 'm\x87xima'],
                'low': ['minima', 'mínima', 'm_nima', 'low', 'm\x92nima'],
                'close': ['fechamento', 'close'],
                'volume': ['volume', 'vol'],
                'sma_20_close_csv': ['orquestrador_moderado_1_visual [0.50 0.40 0.30 0.30 20 3 900 915 20 2.00 0 verdadeiro verdadeiro verdadeiro]'],
                'bb_upper_csv': ['orquestrador_moderado_1_visual [0.50 0.40 0.30 0.30 20 3 900 915 20 2.00 0 verdadeiro verdadeiro verdadeiro].1'],
                'bb_lower_csv': ['orquestrador_moderado_1_visual [0.50 0.40 0.30 0.30 20 3 900 915 20 2.00 0 verdadeiro verdadeiro verdadeiro].2'],
                'first_bar_max_csv': ['orquestrador_moderado_1_visual [0.50 0.40 0.30 0.30 20 3 900 915 20 2.00 0 verdadeiro verdadeiro verdadeiro].3'],
                'first_bar_min_csv': ['orquestrador_moderado_1_visual [0.50 0.40 0.30 0.30 20 3 900 915 20 2.00 0 verdadeiro verdadeiro verdadeiro].4']
            }
            
            # Criar um dicionário de renomeação dinamicamente
            rename_map = {}
            for current_col in data.columns:
                # Não normalizar acentos aqui, pois já estamos lidando com as representações de bytes
                normalized_current_col = current_col.lower()
                for standard_name, candidates in col_candidates.items():
                    if normalized_current_col in candidates or current_col in candidates:
                        rename_map[current_col] = standard_name
                        break
            
            # Adicionar mais prints para depuração
            print("Colunas originais do CSV:", data.columns.tolist())
            data.rename(columns=rename_map, inplace=True)
            print("Colunas após renomeação:", data.columns.tolist())

            # Verificar se as colunas de referência foram carregadas
            ref_cols = ['sma_20_close_csv', 'bb_upper_csv', 'bb_lower_csv']
            for col in ref_cols:
                if col not in data.columns:
                    print(f"AVISO: Coluna de referência '{col}' não encontrada no CSV.")
            
            # Adicionar coluna de volume se não existir, antes da reamostragem
            if 'volume' not in data.columns:
                data['volume'] = 100

            # Filtrar por período se especificado
            if start_date and end_date:
                start = pd.to_datetime(start_date)
                end = pd.to_datetime(end_date)
                data = data[(data.index >= start) & (data.index <= end)]

            # Reamostragem para o tempo gráfico alvo
            if target_interval and target_interval != "1min":
                print(f"Reamostrando dados para {target_interval}...")
                ohlc_dict = {
                    'open': 'first',
                    'high': 'max',
                    'low': 'min',
                    'close': 'last',
                    'volume': 'sum'
                }
                # Preservar colunas de referência, pegando o último valor da janela
                ref_cols = ['sma_20_close_csv', 'bb_upper_csv', 'bb_lower_csv', 'first_bar_max_csv', 'first_bar_min_csv']
                for col in ref_cols:
                    if col in data.columns:
                        ohlc_dict[col] = 'last'
                data = data.resample(target_interval).agg(ohlc_dict)
            
            # Verificar colunas obrigatórias
            required_cols = ['open', 'high', 'low', 'close']
            missing_cols = [col for col in required_cols if col not in data.columns]
            
            if missing_cols:
                raise ValueError(f"Colunas obrigatórias não encontradas após mapeamento: {missing_cols}")
            
            if 'volume' not in data.columns:
                data['volume'] = 100
            
            data = data.dropna()
            
            if len(data) == 0:
                raise ValueError("Nenhum dado válido encontrado após limpeza")
            
            print(f"   Período final: {data.index.min()} até {data.index.max()}")
            # Incluir colunas de referência se existirem
            final_cols = required_cols + ['volume']
            ref_cols = ['sma_20_close_csv', 'bb_upper_csv', 'bb_lower_csv', 'first_bar_max_csv', 'first_bar_min_csv']
            for col in ref_cols:
                if col in data.columns:
                    final_cols.append(col)

            print(f"   Colunas Finais: {final_cols}")
            
            return data[final_cols]
            
        except Exception as e:
            print(f"Erro ao carregar ou reamostrar CSV: {str(e)}")
            raise ValueError(f"Erro no processamento do CSV: {str(e)}")
