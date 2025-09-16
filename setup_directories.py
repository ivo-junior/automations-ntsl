"""
Script para configurar estrutura inicial de diretórios do projeto NTSL
"""

import os
from pathlib import Path

def setup_project_structure():
    """Cria estrutura de diretórios necessária"""
    
    base_dir = Path(__file__).parent.resolve()
    
    directories = [
        base_dir / "backtest" / "dados",
        base_dir / "estrategias" / "automations", 
        base_dir / "estrategias" / "indicadores",
        base_dir / "resultados" / "backtests",
        base_dir / "resultados" / "graficos",
        base_dir / "resultados" / "relatorios"
    ]
    
    print("🔧 CONFIGURANDO ESTRUTURA DO PROJETO")
    print("=" * 40)
    
    for directory in directories:
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)
            print(f"✅ Criado: {directory.relative_to(base_dir)}")
        else:
            print(f"📁 Existe: {directory.relative_to(base_dir)}")
    
    print(f"\n📁 ESTRUTURA FINAL:")
    print(f"📂 {base_dir.name}/")
    print(f"   📂 backtest/")
    print(f"      📂 dados/              ← Colocar arquivos CSV aqui")
    print(f"   📂 estrategias/")
    print(f"      📂 automations/        ← Estratégias NTSL (.txt)")
    print(f"      📂 indicadores/        ← Indicadores NTSL")
    print(f"   📂 resultados/")
    print(f"      📂 backtests/          ← Resultados em Excel/CSV")
    print(f"      📂 graficos/           ← Gráficos de equity") 
    print(f"      📂 relatorios/         ← Relatórios detalhados")
    
    # Criar arquivo de exemplo
    example_strategy = base_dir / "estrategias" / "automations" / "exemplo_simple.txt"
    if not example_strategy.exists():
        example_content = """// Estratégia de exemplo simples
Input
    nomeEstrategia("Exemplo Simples");
    numeroMagico(12345);
    
Var
    posicao: Boolean;
    
begin
    // Lógica da estratégia aqui
end;"""
        
        example_strategy.write_text(example_content, encoding='utf-8')
        print(f"📝 Criado exemplo: {example_strategy.name}")
    
    print(f"\n✅ Configuração concluída!")
    print(f"💡 Execute: python examples/quick_test.py")

if __name__ == "__main__":
    setup_project_structure()
