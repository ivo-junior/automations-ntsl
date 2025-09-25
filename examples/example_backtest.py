"""
Exemplo de uso do sistema de backtest NTSL

Este script demonstra como:
1. Carregar uma estratégia NTSL
2. Obter dados históricos  
3. Executar backtest
4. Analisar resultados
"""

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backtest import NTSLParser, BacktestEngine, DataProvider
import matplotlib.pyplot as plt

def main():
    """Exemplo completo de backtest"""
    
    # 1. Configuração
    strategy_file = r"c:\Dev\automations-ntsl\estrategias\automations\orquestrador_moderado_1.txt"
    symbol = r"C:\Dev\automations-ntsl\backtest\dados\WINFUTV_F_0_1min.csv"
    start_date = "2025-07-29"
    end_date = "2025-09-16"
    interval = "1min" # Intervalo do arquivo CSV original
    source = "local_csv"
    target_interval = "5min" # Intervalo para reamostragem
    
    print("=== SISTEMA DE BACKTEST NTSL ===\n")
    
    # 2. Parsear estratégia
    print("Parseando estratégia...")
    parser = NTSLParser()
    strategy = parser.parse_file(strategy_file)
    
    print(f"Estratégia carregada: {strategy.name}")
    print(f"   Magic Number: {strategy.magic_number}")
    print(f"   Parâmetros de risco: {len(strategy.risk_params)} encontrados\n")
    
    # 3. Obter dados
    print("Obtendo dados históricos...")
    data_provider = DataProvider()
    data = data_provider.get_data(symbol, start_date, end_date, interval, source, target_interval)
    
    print(f"Dados carregados: {len(data)} barras")
    print(f"   Período: {data.index[0]} a {data.index[-1]}")
    print(f"   Preço inicial: {data['close'].iloc[0]:.2f}")
    print(f"   Preço final: {data['close'].iloc[-1]:.2f}\n")
    
    # 4. Executar backtest
    print("Executando backtest...")
    engine = BacktestEngine()
    result = engine.run_backtest(strategy, data, asset="WINFUT", timeframe="5m")
    
    # 5. Análise de resultados
    print("\n" + "="*50)
    print("RESULTADOS DO BACKTEST")
    print("="*50)
    
    metrics = result.metrics

    if not metrics:
        print("Nenhuma operação executada para o período selecionado.")
        return
    
    print(f"Saldo Líquido Total: R$ {metrics['net_profit']:.2f}")
    print(f"Lucro Bruto: R$ {metrics['gross_profit']:.2f}")  
    print(f"Prejuízo Bruto: R$ {metrics['gross_loss']:.2f}")
    print(f"Fator de Lucro: {metrics['profit_factor']:.2f}")
    print(f"Número total de operações: {metrics['total_trades']}")
    print(f"Operações vencedoras: {metrics['winning_trades']}")
    print(f"Operações perdedoras: {metrics['losing_trades']}")
    print(f"Percentual de acerto: {metrics['win_rate']:.1f}%")
    print(f"Resultado médio por trade: R$ {metrics['avg_trade']:.2f}")
    
    # 6. Comparação com resultado informado
    print(f"\nCOMPARAÇÃO COM RESULTADO PROFIT PRO:")
    # print(f"Resultado esperado: R$ 717,00")
    # print(f"Resultado obtido: R$ {metrics['net_profit']:.2f}")
    # diferenca = metrics['net_profit'] - 717
    # print(f"Diferença: R$ {diferenca:.2f} ({diferenca/717*100:+.1f}%)")
    
    # 7. Gráfico da curva de equity (opcional)
    if len(result.equity_curve) > 0:
        plt.figure(figsize=(12, 6))
        plt.plot(result.equity_curve.index, result.equity_curve.values)
        plt.title(f'Curva de Equity - {strategy.name}')
        plt.xlabel('Data')
        plt.ylabel('Resultado Acumulado (R$)')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Salvar gráfico
        chart_path = f"equity_curve_{strategy.name}_{os.path.basename(symbol)}.png"
        plt.savefig(chart_path)
        print(f"\nGráfico salvo: {chart_path}")
        
        # Mostrar gráfico se disponível
        try:
            plt.show()
        except:
            print("   (Interface gráfica não disponível)")
    
    # 8. Lista de trades detalhada
    print(f"TRADES EXECUTADOS ({len(result.trades)} operações):")
    print("-" * 80)
    for i, trade in enumerate(result.trades[:10]):  # Mostrar apenas primeiros 10
        print(f"{i+1:2d}. {trade.direction:5s} | Qtd: {trade.quantity:2d} | "
              f"{trade.entry_time.strftime('%d/%m %H:%M')} -> "
              f"{trade.exit_time.strftime('%d/%m %H:%M') if trade.exit_time else 'ABERTO':11s} | "
              f"R$ {trade.result:8.2f}")
    
    if len(result.trades) > 10:
        print(f"... e mais {len(result.trades) - 10} operações")

if __name__ == "__main__":
    main()