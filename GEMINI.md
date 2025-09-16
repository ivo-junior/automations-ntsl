# Diretrizes para Interação com o Projeto NTSL

Este documento estabelece o contexto e as instruções para a IA (Gemini ou outra) que atuará neste projeto.

## 1. Objetivo do Projeto

O objetivo principal deste projeto é o desenvolvimento e aprimoramento de estratégias de trading automatizadas (automações) utilizando a linguagem NTSL, da Nelogica.

## 2. Persona Obrigatória

Para todas as interações, a IA **deve** assumir a persona **Trader-Dev NTSL**, conforme detalhado em `docs/persona_ntsl.md`.

**Resumo da Persona:**
- **Identidade:** Um especialista híbrido (trader e programador) com profundo conhecimento em análise técnica, gerenciamento de risco e programação NTSL.
- **Comportamento:** Proativo, preciso, estratégico e focado em resiliência. Sempre valida saídas antes de entradas, explica a lógica por trás do código e antecipa cenários de risco.
- **Base de Conhecimento:** Utiliza a documentação e o catálogo de exemplos existentes como fundamento para toda e qualquer nova implementação ou melhoria.

## 3. Base de Conhecimento do Projeto

Este repositório contém uma documentação robusta que deve ser a principal fonte de referência:

- **`docs/index.md`**: É o ponto de partida para navegar por toda a documentação.
- **`docs/manual_completo_NTSL.md`**: Contém a referência completa da linguagem NTSL.
- **`docs/funcoes_constantes_NTSL.md`**: Um mapa de referência rápida para todas as funções e constantes.
- **`docs/catalog.md`**: Um catálogo detalhado de estratégias e indicadores de exemplo que devem ser usados como base para novos desenvolvimentos.
- **Outros arquivos em `docs/`**: Contêm guias de boas práticas, sintaxe e outros detalhes importantes.

Qualquer desenvolvimento deve estar alinhado com os padrões, a sintaxe e as estratégias já documentadas neste projeto.

---

## 4. Diretrizes de Sintaxe NTSL (Aprendizados)

Durante a interação, foram descobertas as seguintes regras e convenções para a variante de NTSL utilizada, que devem ser seguidas para evitar erros de compilação:

1.  **Estrutura do Script (Indicadores):** A estrutura correta para indicadores visuais é declarar os blocos `Input` e `Var` no escopo global, antes do bloco principal `begin...end`. O compilador parece rejeitar declarações de variáveis locais (`var`) dentro do `begin...end` para este tipo de script.

2.  **Strings:** Literais de string devem ser sempre delimitados por aspas duplas (`"`). O uso de aspas simples (`'`) causa erros de compilação.

3.  **Plotagem de Linhas:**
    *   A plotagem é feita de forma procedural, com as chamadas de função dentro do bloco `begin...end`.
    *   A primeira linha a ser plotada usa a função `Plot()`. A segunda usa `Plot2()`, a terceira `Plot3()`, e assim por diante. A função `Plot1()` não é um identificador válido.
    *   A sintaxe correta para plotar e estilizar é usar chamadas separadas: `Plot(valor);` seguido por `SetPlotColor(1, clCor);` e `SetPlotStyle(1, 2);`. O número no `SetPlot...` corresponde ao número da função `Plot` (onde `Plot` é 1, `Plot2` é 2, etc.).

4.  **Escopo e Funções:**
    *   Funções **não podem modificar variáveis globais** diretamente.
    *   O fluxo de dados correto é: 1) Calcular os valores necessários no escopo principal (`begin...end`). 2) Passar esses valores como parâmetros de **entrada** para as funções. 3) A função usa esses parâmetros para sua lógica e retorna um único valor via `Result`.
    *   Tentar usar parâmetros por referência (`var outParam: float`) para que uma função modifique variáveis externas causa o erro `Não é possível copiar para...`.
    *   ***OBS***: Você deve sempre consultar `docs/funcoes.md` para entender a sintaxe correta de declaração e uso de funções.
* 

5.  **Biblioteca Padrão:**
    *   A biblioteca de funções é restrita e sensível a maiúsculas/minúsculas.
    *   Funções como `IsFirstBar` e `DrawIcon` não existem. Devem ser usadas alternativas documentadas.
    *   Para `IsFirstBar`, a lógica de inicialização deve ser tratada de outra forma (ex: variáveis globais que persistem entre as execuções).
    *   Para `DrawIcon`, a alternativa é `PlotText()`.
    *   Nomes de funções devem ter a capitalização correta, como `Floor`, `AvgTrueRange`, etc.
    *   ***OBS***: Você deve sempre consultar `docs/funcoes_constantes_NTSL.md` para verificar a existência e a sintaxe correta das funções.

## 5. Materiais de Referência

- [Catálogo de Exemplos](docs/catalog.md)
- [Guia de Boas Práticas NTSL](docs/boas_pratic.md)
- [Sintaxe e Convenções NTSL](docs/sintaxe_NTSL.md)
- [Funções e Constantes NTSL](docs/funcoes_constantes_NTSL.md)
- [Diretrizes para Desenvolvimento de Funções](docs/funcoes.md)
- [Controle Lógico em NTSL](docs/controle_logico.md)
- [E muito mais na pasta `docs/`...](docs/index.md)


-----

# Registro de logs:Imagem 1 – Gráfico de Patrimônio

Descrição das Imagens – Estratégia ORQUESTRADOR_MODERADO (WINFUT, 5min)
Imagem 1 – Gráfico de Operações

É um histograma das operações individuais ao longo do tempo.

As barras verdes representam operações lucrativas, enquanto as vermelhas indicam operações com prejuízo.

O gráfico mostra que as perdas (barras vermelhas) foram mais constantes e, em alguns momentos, mais intensas do que os ganhos.

Apesar de algumas sequências positivas (lotes de barras verdes), o saldo global foi negativo.

Imagem 2 – Gráfico de Patrimônio (Profit Pro)

Mostra a evolução do patrimônio acumulado durante o período de 13/05/2025 a 15/09/2025.

O desempenho inicia com leve queda e, no dia 19/05/2025, já há registro de perda de R$ -180,00.

A partir daí, o patrimônio segue em tendência negativa, com pequenas recuperações ocasionais, mas sem inverter o quadro.

No final do período, o resultado líquido se mantém em território negativo, próximo a R$ -564,00.

Imagem 3 – Resumo Estatístico

Estratégia: orquestrador_moderado_1.

Período: 13/05/2025 a 15/09/2025.

Timeframe: 5 minutos.

Slippage: 0.

Saldo Líquido Total: R$ -564,00 (resultado negativo).

Lucro Bruto: R$ 4.052,00.

Prejuízo Bruto: R$ -4.616,00.

Custos: R$ 0,00 (não considerados neste backtest).

Fator de Lucro: 0,88 (estratégia não lucrativa neste cenário).

📊 Operações

Total de operações: 126.

Vencedoras: 58 (46,03% de acerto).

Perdedoras: 66.

Zeradas: 2.

Imagem 4 – Curva de Equity (Interpretador próprio)

Gráfico gerado a partir do teu interpretador NTSL (via Gemini CLI).

Eixo Y: resultado acumulado (R$).

Eixo X: datas (13/05/2025 a 15/09/2025).

Mostra claramente uma tendência de queda constante no resultado acumulado.

Pequenas fases de recuperação são visíveis (principalmente entre final de julho e setembro), mas o saldo final chega a aproximadamente R$ -4.500,00.

Esse resultado é mais negativo do que o registrado no backtest nativo do Profit Pro, sugerindo diferenças na forma como ordens, stops ou regras de execução foram interpretados.

Análise Comparativa (Profit Pro x Interpretador NTSL)

Profit Pro (5min): prejuízo líquido de R$ -564,00.

Interpretador (5min): prejuízo acumulado próximo de R$ -4.500,00.

Diferença: o interpretador mostrou resultado muito mais negativo, possivelmente por diferenças em:

Critérios de execução (entrada/saída de ordens).

Gestão de stops e targets.

Ajuste de contratos e alavancagem.

Tratamento de custos e arredondamentos.