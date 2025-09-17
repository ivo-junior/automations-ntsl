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

## Ajustes Realizados no Backtest

- **Custo por Operação:** O custo por operação foi fixado em `0.23` (entrada + saída) no arquivo `backtest/backtest_engine.py` para alinhar com os custos operacionais reais informados, substituindo o valor de `0.85` que estava no arquivo da estratégia e o valor `0.0` usado temporariamente para depuração.

## Abaixo estão algumas citações de Jesse Livermore. Esses conselhos representam a experiência de um trader que enfrentou diversas situações, inclusive o famoso crash de 1929:


- Nunca opere baseado em dicas;
- Use um sistema e não saia dele;
- Nunca compre uma ação porque ela teve uma grande queda da sua última alta;
- Se uma ação não agir corretamente não toque-a; porque, não podendo dizer precisamente o que está errado, você não pode dizer para que lado ela irá;
- Não culpe o mercado pelas suas perdas;
- Nunca aumente uma posição perdedora. Uma posição perdedora siginifica que você está errado;
- Ações nunca estão muito altas para começar a comprar nem muito baixas para começar a vender. Mas depois da primeira transação, não faça uma segunda a não ser que a primeira mostre lucro;
- Sempre venda o que mostra um prejuízo, e mantenha o que está dando lucro;
- Não discuta com o mercado. Não procure recuperar o prejuízo. Saia enquanto a saída é boa - e barata;
- Existe somente um lado no mercado financeiro. E não é o lado bull (alta) e nem o lado bear (baixa) mas o lado certo;
- O maior inimigo de um especulador é sempre o tédio.
- Um homem deve sempre confiar em si mesmo e no seu julgamento se ele espera ganhar a vida com essa profissão;
- Sempre use gerenciamento de capital;
- Estabeleça o seu plano de trade antes que o mercado abra;
- Detalhe o seu plano para cada trade;
- Estabeleça pontos de entrada e saída e entenda a relação entre risco e recompensa;
- Estabeleça pontos de entrada e saída e entenda a relação entre risco e recompensa;
- Aceite pequenas perdas como parte do jogo se você quiser vencer;
- Desenvolva um plano de trade para cada situação que você pode vir a enfrentar;
- Não concentre-se no valor em que você empata quando estiver perdendo;
- Não liquide uma posição vencedora para manter uma perdedora;
- Desenvolva e mantenha um plano de saída., Siga esse plano com rígida disciplina;
- Tenha paciência. Grandes movimentos demoram para se desenrolar;
- Não fique curioso demais sobre a lógica por trás de um movimento. A chave para a fortuna no mercado é a simplicidade.

# Resultados do Profit Pro no período de 29/07/2025 a 16/09/2025
📊 Timeframe 1 Minuto

>>Resumo Principal
Saldo Líquido Total: R$ 27,00
Fator de Lucro: 1,02
Percentual de Acerto: 46,46%
Total de Operações: 99

>>Detalhes Financeiros
Lucro Bruto: R$ 1.596,00
Prejuízo Bruto: R$ -1.569,00
Custos Totais: R$ 0,00

>>talhes Operacionais
Operações Vencedoras: 46
Operações Perdedoras: 52
Média por Trade: R$ 0,27
Média Ganho / Média Perda: 1,15

---

📊 Timeframe 5 Minutos

>>Resumo Principal
Saldo Líquido Total: R$ 281,00
Fator de Lucro: 1,16
Percentual de Acerto: 51,72%
Total de Operações: 58

>>Detalhes Financeiros
Lucro Bruto: R$ 2.029,00
Prejuízo Bruto: R$ -1.748,00
Custos Totais: R$ 0,00

>>Detalhes Operacionais
Operações Vencedoras: 30
Operações Perdedoras: 26
Média por Trade: R$ 4,84
Média Ganho / Média Perda: 1,01

📊 Timeframe 10 Minutos

>>Resumo Principal
Saldo Líquido Total: R$ 473,00
Fator de Lucro: 1,28
Percentual de Acerto: 44,44%
Total de Operações: 45

>>Detalhes Financeiros
Lucro Bruto: R$ 2.136,00
Prejuízo Bruto: R$ -1.663,00
Custos Totais: R$ 0,00

>>Detalhes Operacionais
Operações Vencedoras: 20
Operações Perdedoras: 23
Média por Trade: R$ 10,51
Média Ganho / Média Perda: 1,48

📊 Timeframe 15 Minutos

Resumo Principal
>>Saldo Líquido Total: R$ 616,00
Fator de Lucro: 1,42
Percentual de Acerto: 47,22%
Total de Operações: 36

>>Detalhes Financeiros
Lucro Bruto: R$ 2.072,00
Prejuízo Bruto: R$ -1.456,00
Custos Totais: R$ 0,00

>>Detalhes Operacionais
Operações Vencedoras: 17
Operações Perdedoras: 19
Média por Trade: R$ 17,11
Média Ganho / Média Perda: 1,59

📊 Timeframe 30 Minutos

>>Resumo Principal
Saldo Líquido Total: R$ 291,00
Fator de Lucro: 1,18
Percentual de Acerto: 52,38%
Total de Operações: 21

>>Detalhes Financeiros
Lucro Bruto: R$ 1.953,00
Prejuízo Bruto: R$ -1.662,00
Custos Totais: R$ 0,00

>>Detalhes Operacionais
Operações Vencedoras: 11
Operações Perdedoras: 10
Média por Trade: R$ 13,86
Média Ganho / Média Perda: 1,07