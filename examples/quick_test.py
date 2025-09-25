"""
Script para teste rápido do sistema de backtest

Uso:
python quick_test.py
"""

import sys
import os
from pathlib import Path

# Adicionar path do projeto
sys.path.append(str(Path(__file__).parent.parent))

from backtest.console_runner import ConsoleRunner

def test_orquestrador():
    """Teste específico do orquestrador moderado"""
    
    runner = ConsoleRunner()
    
    print("🧪 TESTE RÁPIDO - SISTEMA DE BACKTEST NTSL")
    print("=" * 50)
    
    # Sistema de seleção interativa
    runner.run_interactive()

def test_batch_example():
    """Exemplo de teste em batch com arquivos específicos"""
    
    runner = ConsoleRunner()
    
    # Exemplo de paths (ajustar conforme necessário)
    strategy_path = "automations/orquestrador_moderado_1.txt"
    data_path = "dados/WINQ23_15min_ago2024.csv"  # exemplo
    
    print("🤖 TESTE EM BATCH")
    print("=" * 30)
    
    try:
        result = runner.run_batch(
            strategy_path=strategy_path,
            data_path=data_path,
            start_date="2024-08-14",
            end_date="2024-09-14"
        )
        
        if result:
            print("✅ Backtest executado com sucesso!")
            print(f"💰 Resultado: R$ {result.metrics.get('net_profit', 0):.2f}")
        else:
            print("❌ Erro no backtest batch")
            
    except Exception as e:
        print(f"❌ Erro: {str(e)}")

if __name__ == "__main__":
    # Executar teste interativo por padrão
    test_orquestrador()
    
    # Uncomment para testar modo batch
    # test_batch_example()
