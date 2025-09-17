# ================================================================
# MAKEFILE PARA SISTEMA DE BACKTEST NTSL
# ================================================================
# Este Makefile facilita o uso do sistema de backtest NTSL
# com comandos simples e organizados.
#
# Uso:
#   make setup     - Configura estrutura inicial do projeto
#   make test      - Executa teste rápido interativo
#   make batch     - Executa backtest em modo batch
#   make deps      - Instala dependências Python
#   make clean     - Limpa arquivos temporários
#   make help      - Mostra esta ajuda

# ================================================================
# CONFIGURAÇÕES
# ================================================================

# Diretórios do projeto
PROJECT_ROOT ?= .
BACKTEST_DIR := $(PROJECT_ROOT)/backtest
STRATEGIES_DIR := $(PROJECT_ROOT)/estrategias/automations
DATA_DIR := $(BACKTEST_DIR)/dados
RESULTS_DIR := $(PROJECT_ROOT)/resultados

# Arquivos Python principais
CONSOLE_RUNNER := $(BACKTEST_DIR)/console_runner.py
QUICK_TEST := $(PROJECT_ROOT)/examples/quick_test.py
SETUP_SCRIPT := $(PROJECT_ROOT)/setup_directories.py

# Configurações padrão para batch
STRATEGY ?= orquestrador_moderado_1.txt
DATA ?= dados_exemplo.csv
START ?= 2024-08-14
END ?= 2024-09-14

# ================================================================
# COMANDOS PRINCIPAIS
# ================================================================

.PHONY: help setup test batch deps clean install list-strategies list-data

# Comando padrão
all: help

# Ajuda
help:
	@echo "================================================================"
	@echo "🚀 SISTEMA DE BACKTEST NTSL - COMANDOS DISPONÍVEIS"
	@echo "================================================================"
	@echo ""
	@echo "📋 COMANDOS PRINCIPAIS:"
	@echo "  make setup          - Configura estrutura inicial do projeto"
	@echo "  make test           - Executa teste rápido interativo"
	@echo "  make batch          - Executa backtest em modo batch"
	@echo "  make deps           - Instala dependências Python"
	@echo ""
	@echo "📊 COMANDOS DE DADOS:"
	@echo "  make list-strategies - Lista estratégias disponíveis"
	@echo "  make list-data      - Lista arquivos CSV disponíveis"
	@echo ""
	@echo "🧹 COMANDOS DE MANUTENÇÃO:"
	@echo "  make clean          - Limpa arquivos temporários"
	@echo "  make install        - Instalação completa (setup + deps)"
	@echo ""
	@echo "📁 ESTRUTURA DO PROJETO:"
	@echo "  📂 estrategias/automations/  ← Estratégias NTSL (.txt)"
	@echo "  📂 backtest/dados/           ← Dados CSV"
	@echo "  📂 resultados/               ← Resultados dos backtests"
	@echo ""
	@echo "💡 EXEMPLOS DE USO:"
	@echo "  make test                                    # Teste interativo"
	@echo "  make batch STRATEGY=minha_estrategia.txt     # Batch específico"
	@echo "  make batch DATA=meus_dados.csv               # Com dados específicos"
	@echo ""

# ================================================================
# CONFIGURAÇÃO E INSTALAÇÃO
# ================================================================

# Configurar estrutura do projeto
setup:
	@echo "🔧 Configurando estrutura do projeto..."
	@if not exist "$(PROJECT_ROOT)" mkdir "$(PROJECT_ROOT)"
	@python "$(SETUP_SCRIPT)"
	@echo "✅ Estrutura configurada com sucesso!"

# Instalar dependências Python
deps:
	@echo "📦 Instalando dependências Python..."
	@python -m pip install --upgrade pip
	@	@python -m pip install -r requirements.txt
	@echo "✅ Dependências instaladas!"

# Instalação completa
install: setup deps
	@echo "🎉 Instalação completa finalizada!"
	@echo "💡 Execute 'make test' para começar a usar o sistema"

# ================================================================
# EXECUÇÃO DE BACKTESTS
# ================================================================

# Teste rápido interativo
test:
	@echo "🧪 Executando teste interativo..."
	@cd "$(PROJECT_ROOT)" && python -m examples.quick_test

# Execução em modo batch
batch:
	echo "🤖 Executando backtest em modo batch..."
		cd "$(PROJECT_ROOT)" && set PYTHONIOENCODING=UTF-8 && python -m backtest.console_runner --batch \
			--strategy "$(STRATEGIES_DIR)/$(STRATEGY)" \
			--data "$(DATA_DIR)/$(DATA)" \
			--start-date "$(START)" \
			--end-date "$(END)" \
			--output "$(RESULTS_DIR)/backtests" \
			--timeframe "$(TIMEFRAME)"

# Execução batch com parâmetros personalizados
batch-custom:
	@echo "🎯 Backtest customizado:"
	@echo "   Estratégia: $(STRATEGY)"
	@echo "   Dados: $(DATA)"
	@echo "   Período: $(START) a $(END)"
	@cd "$(PROJECT_ROOT)" && python -m backtest.console_runner --batch \
		--strategy "$(STRATEGY)" \
		--data "$(DATA)" \
		--start-date "$(START)" \
		--end-date "$(END)" \
		--output "$(OUTPUT)"

# ================================================================
# COMANDOS DE LISTAGEM E INFORMAÇÃO
# ================================================================

# Listar estratégias disponíveis
list-strategies:
	@echo "📋 ESTRATÉGIAS NTSL DISPONÍVEIS:"
	@echo "================================"
	@if exist "$(STRATEGIES_DIR)" (
		@for /r "$(STRATEGIES_DIR)" %%f in (*.txt) do @echo "   %%~nxf"
	) else (
		@echo "❌ Diretório de estratégias não encontrado"
		@echo "💡 Execute 'make setup' para criar a estrutura"
	)

# Listar dados CSV disponíveis
list-data:
	@echo "📊 ARQUIVOS CSV DISPONÍVEIS:"
	@echo "============================"
	@if exist "$(DATA_DIR)" (
		@for %%f in ("$(DATA_DIR)\*.csv") do @echo "   %%~nxf"
	) else (
		@echo "❌ Diretório de dados não encontrado"
		@echo "💡 Execute 'make setup' para criar a estrutura"
	)

# Mostrar status do projeto
status:
	@echo "📈 STATUS DO PROJETO BACKTEST NTSL"
	@echo "=================================="
	@echo "📁 Projeto: $(PROJECT_ROOT)"
	@if exist "$(PROJECT_ROOT)" (
		@echo "✅ Diretório principal: OK"
	) else (
		@echo "❌ Diretório principal: NÃO ENCONTRADO"
	)
	@if exist "$(STRATEGIES_DIR)" (
		@echo "✅ Diretório estratégias: OK"
	) else (
		@echo "❌ Diretório estratégias: NÃO ENCONTRADO"
	)
	@if exist "$(DATA_DIR)" (
		@echo "✅ Diretório dados: OK"
	) else (
		@echo "❌ Diretório dados: NÃO ENCONTRADO"
	)

# ================================================================
# COMANDOS DE DESENVOLVIMENTO E DEBUG
# ================================================================

# Executar com debug
debug:
	@echo "🐛 Executando em modo debug..."
	@cd "$(PROJECT_ROOT)" && python -u "$(CONSOLE_RUNNER)" --debug

# Validar estrutura de arquivo NTSL
validate:
	@if "$(STRATEGY)" == "" (
		@echo "❌ Especifique a estratégia: make validate STRATEGY=arquivo.txt"
	) else (
		@echo "🔍 Validando estratégia: $(STRATEGY)"
		@cd "$(PROJECT_ROOT)" && python -c "from backtest.ntsl_parser import NTSLParser; parser = NTSLParser(); strategy = parser.parse_file('$(STRATEGIES_DIR)\\$(STRATEGY)'); print(f'✅ Estratégia válida: {strategy.name}')"
	)

# Testar conexão com dados
test-data:
	@if "$(DATA)" == "" (
		@echo "❌ Especifique o arquivo: make test-data DATA=arquivo.csv"
	) else (
		@echo "📊 Testando dados: $(DATA)"
		@cd "$(PROJECT_ROOT)" && python -c "from backtest.data_provider import DataProvider; dp = DataProvider(); data = dp._get_local_csv_data('$(DATA_DIR)\\$(DATA)', None, None); print(f'✅ Dados válidos: {len(data)} barras')"
	)

# ================================================================
# COMANDOS DE LIMPEZA E MANUTENÇÃO
# ================================================================

# Limpar arquivos temporários
clean:
	@echo "🧹 Limpando arquivos temporários..."
	@if exist "$(PROJECT_ROOT)\__pycache__" rmdir /s /q "$(PROJECT_ROOT)\__pycache__"
	@if exist "$(BACKTEST_DIR)\__pycache__" rmdir /s /q "$(BACKTEST_DIR)\__pycache__"
	@for /r "$(PROJECT_ROOT)" %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d" 2>nul
	@for /r "$(PROJECT_ROOT)" %%f in (*.pyc) do @del "%%f" 2>nul
	@for /r "$(PROJECT_ROOT)" %%f in (*.pyo) do @del "%%f" 2>nul
	@echo "✅ Limpeza concluída!"

# Limpar resultados antigos
clean-results:
	@echo "🗑️ Limpando resultados antigos..."
	@if exist "$(RESULTS_DIR)" (
		@for /f %%f in ('dir /b "$(RESULTS_DIR)\backtests\*.xlsx" 2^>nul') do @del "$(RESULTS_DIR)\backtests\%%f"
		@for /f %%f in ('dir /b "$(RESULTS_DIR)\backtests\*.csv" 2^>nul') do @del "$(RESULTS_DIR)\backtests\%%f"
		@for /f %%f in ('dir /b "$(RESULTS_DIR)\graficos\*.png" 2^>nul') do @del "$(RESULTS_DIR)\graficos\%%f"
	)
	@echo "✅ Resultados antigos removidos!"

# ================================================================
# COMANDOS ESPECIAIS E EXEMPLOS
# ================================================================

# Exemplo completo com orquestrador moderado
example-orquestrador:
	@echo "🎯 EXEMPLO: Backtest do Orquestrador Moderado"
	@echo "============================================"
	make batch STRATEGY=orquestrador_moderado_1.txt START=2024-08-14 END=2024-09-14

# Executar múltiplos backtests
batch-all:
	@echo "🔄 Executando backtests para todas as estratégias..."
	@for %%f in ("$(STRATEGIES_DIR)\*.txt") do @(
		@echo "📊 Testando: %%~nxf"
		@make batch STRATEGY=%%~nxf
	)

# Benchmark de performance
benchmark:
	@echo "⚡ Executando benchmark de performance..."
	@echo "Iniciado em: %date% %time%"
	@cd "$(PROJECT_ROOT)" && python -c "import time; start = time.time(); exec(open('examples/quick_test.py').read()); print(f'Tempo total: {time.time()-start:.2f}s')"

# ================================================================
# COMANDOS DE RELATÓRIOS
# ================================================================

# Gerar relatório de estratégias
report-strategies:
	@echo "📋 RELATÓRIO DE ESTRATÉGIAS" > "$(RESULTS_DIR)\strategy_report.txt"
	@echo "==========================" >> "$(RESULTS_DIR)\strategy_report.txt"
	@echo "Gerado em: %date% %time%" >> "$(RESULTS_DIR)\strategy_report.txt"
	@echo "" >> "$(RESULTS_DIR)\strategy_report.txt"
	@for %%f in ("$(STRATEGIES_DIR)\*.txt") do @echo "- %%~nxf" >> "$(RESULTS_DIR)\strategy_report.txt"
	@echo "✅ Relatório salvo em: $(RESULTS_DIR)\strategy_report.txt"

# ================================================================
# COMANDOS AVANÇADOS
# ================================================================

# Setup para desenvolvimento
dev-setup: setup deps
	@echo "🔧 Configuração para desenvolvimento..."
	@python -m pip install pytest black flake8
	@echo "✅ Ambiente de desenvolvimento configurado!"

# Executar testes unitários (quando implementados)
test-unit:
	@echo "🧪 Executando testes unitários..."
	@cd "$(PROJECT_ROOT)" && python -m pytest tests/ -v

# Formatar código Python
format:
	@echo "✨ Formatando código Python..."
	@python -m black "$(BACKTEST_DIR)"
	@python -m black "$(PROJECT_ROOT)\examples"
	@echo "✅ Código formatado!"

# Verificar qualidade do código
lint:
	@echo "🔍 Verificando qualidade do código..."
	@python -m flake8 "$(BACKTEST_DIR)" --max-line-length=100
	@echo "✅ Verificação concluída!"
