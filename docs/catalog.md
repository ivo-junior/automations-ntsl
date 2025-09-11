'''# Catálogo de Estratégias e Indicadores NTSL

Este documento cataloga e descreve as estratégias e indicadores contidos na pasta `estrategias/exemplos/editaveis`.

## Intenção do Catálogo

O objetivo deste catálogo é duplo:
1.  **Organizar o Conhecimento:** Estruturar a vasta coleção de scripts NTSL em categorias lógicas, facilitando a busca e a compreensão de implementações existentes.
2.  **Base para Desenvolvimento:** Servir como uma base de conhecimento detalhada para o desenvolvimento de novas automações e para a melhoria das existentes, permitindo que um LLM compreenda rapidamente a lógica de cada script.

## Índice de Navegação

### 🤖 Automações (Estratégias de Trading)
- [Cruzamento de Médias](#cruzamento-de-médias) - Estratégias baseadas no cruzamento de médias móveis
- [Price Action](#price-action) - Estratégias baseadas em análise de price action e padrões de candles
- [Reversão à Média](#reversão-à-média) - Estratégias que operam na reversão de movimentos extremos
- [Rompimento](#rompimento) - Estratégias que operam rompimentos de níveis e canais
- [Scalping](#scalping) - Estratégias de operações rápidas e frequentes
- [Seguidor de Tendência](#seguidor-de-tendência) - Estratégias que seguem a direção da tendência
- [Tendência](#tendência-1) - Estratégias gerais de tendência

### 📊 Indicadores (Análise e Visualização)
- [Outros](#outros) - Indicadores diversos e ferramentas auxiliares
- [Osciladores](#osciladores) - Indicadores de momentum e oscilação
- [Price Action](#price-action-1) - Indicadores de análise técnica e níveis de preço
- [Tendência](#tendência-2) - Indicadores de identificação e acompanhamento de tendência
- [Volatilidade](#volatilidade) - Indicadores de medição de volatilidade e risco
- [Volume](#volume) - Indicadores baseados em análise de volume

### 📈 Estatísticas do Catálogo
- **📋 Total de itens catalogados:** 331
- **🤖 Automações (Estratégias):** 84
- **📊 Indicadores:** 247

### 📁 Estatísticas da Organização de Arquivos
- **📂 Total de arquivos organizados:** 398
- **🤖 Automações organizadas:** 72 arquivos
- **📊 Indicadores organizados:** 326 arquivos

#### Distribuição por Categoria - Automações
- **Cruzamento de Médias:** 6 arquivos
- **Price Action:** 14 arquivos  
- **Reversão à Média:** 16 arquivos
- **Rompimento:** 11 arquivos
- **Diversos:** 11 arquivos
- **Seguidor de Tendência:** 8 arquivos
- **Tendência:** 3 arquivos
- **Osciladores:** 2 arquivos
- **Scalping:** 1 arquivo

#### Distribuição por Categoria - Indicadores
- **Tendência:** 93 arquivos
- **Price Action:** 72 arquivos
- **Volume:** 69 arquivos
- **Osciladores:** 56 arquivos
- **Outros:** 21 arquivos
- **Volatilidade:** 15 arquivos

### 🔍 Como Usar Este Catálogo
1. **Navegação:** Use os links do índice acima para ir diretamente à seção desejada
2. **Busca:** Use `Ctrl+F` (ou `Cmd+F`) para buscar por nomes específicos de indicadores ou estratégias
3. **Categorização:** Cada item está organizado por sua funcionalidade principal
4. **Descrições:** Cada entrada inclui uma breve descrição de sua funcionalidade e comportamento
5. **Tags:** Use as tags de filtro abaixo para encontrar rapidamente scripts específicos

### 🏷️ Sistema de Tags e Filtros

#### Filtros por Complexidade
- `#iniciante` - Scripts simples, ideais para quem está começando
- `#intermediario` - Scripts com lógica moderada
- `#avancado` - Scripts complexos com múltiplas condições

#### Filtros por Timeframe Recomendado
- `#intraday` - Melhor para operações intradia
- `#swing` - Adequado para swing trade
- `#day-trade` - Específico para day trade
- `#multi-timeframe` - Funciona em múltiplos timeframes

#### Filtros por Tipo de Mercado
- `#trending` - Funciona melhor em mercados com tendência
- `#sideways` - Adequado para mercados laterais
- `#volatile` - Requer alta volatilidade
- `#low-volatility` - Funciona em baixa volatilidade

#### Filtros por Performance Estimada
- `#alto-retorno` - Potencial de alto retorno
- `#baixo-risco` - Estratégias mais conservadoras
- `#high-frequency` - Alta frequência de sinais
- `#selective` - Poucos sinais, mas seletivos

#### Filtros por Indicadores Base
- `#rsi` - Baseado no RSI
- `#macd` - Usa MACD
- `#bollinger` - Usa Bandas de Bollinger
- `#moving-average` - Baseado em médias móveis
- `#volume` - Incorpora análise de volume
- `#price-action` - Foco em price action puro

---

## 📊 Índice por Performance e Popularidade

### 🏆 Top Estratégias Recomendadas

#### Alto Potencial de Retorno (`#alto-retorno`)
- **[MILIONARIO_RENKO](estrategias/exemplos/editaveis/automations/seguidor_de_tendencia/MILIONARIO_RENKO.txt)** `#avancado` `#trending` `#alto-retorno`
- **[BollingerBreakout](estrategias/exemplos/editaveis/automations/rompimento/BollingerBreakout.txt)** `#intermediario` `#volatile` `#alto-retorno` `#bollinger`
- **[GridDinamico_RegressaoLinear](estrategias/exemplos/editaveis/automations/reversao_a_media/GridDinamico_RegressaoLinear.txt)** `#avancado` `#sideways` `#alto-retorno`

#### Estratégias Conservadoras (`#baixo-risco`)
- **[2MV_Padrao](estratégias/exemplos/editaveis/automations/cruzamento_de_medias/2MV_Padrao.txt)** `#iniciante` `#baixo-risco` `#moving-average`
- **[Pisani_Stocastic](estrategias/exemplos/editaveis/automations/reversao_a_media/Pisani_Stocastic.txt)** `#intermediario` `#baixo-risco` `#selective`

#### Day Trade Eficientes (`#day-trade`)
- **[STP0003_Trade_e_Acoes_Setup_Larry_Williams_Classico](estrategias/exemplos/editaveis/automations/price_action/STP0003_Trade_e_Acoes_Setup_Larry_Williams_Classico.txt)** `#intermediario` `#day-trade` `#price-action`
- **[V0061_STORMER_901](estrategias/exemplos/editaveis/automations/price_action/V0061_STORMER_901.txt)** `#avancado` `#day-trade` `#high-frequency`

#### Scalping Rápido (`#high-frequency`)
- **[KASTR_SCALP_12R](estrategias/exemplos/editaveis/automations/scalping/KASTR_SCALP_12R.txt)** `#avancado` `#intraday` `#high-frequency` `#volatile`

### 📈 Top Indicadores Mais Úteis

#### Osciladores Populares
- **[Connors_RSI](estrategias/exemplos/editaveis/indicadores/osciladores/Connors_RSI.txt)** `#intermediario` `#rsi` `#multi-timeframe`
- **[TTM_Squeeze](estrategias/exemplos/editaveis/indicadores/osciladores/V0040_TTM_Squeeze.txt)** `#avancado` `#bollinger` `#trending`
- **[WaveTrend_Oscillator](estrategias/exemplos/editaveis/indicadores/osciladores/V0028_WaveTrend_Oscillator.txt)** `#intermediario` `#trending` `#multi-timeframe`

#### Volume e Liquidez
- **[Better_Volume_Original](estrategias/exemplos/editaveis/indicadores/outros/Better_Volume_Original.txt)** `#intermediario` `#volume` `#multi-timeframe`
- **[Volume_Flow_Indicator](estrategias/exemplos/editaveis/indicadores/volume/Volume_Flow_Indicator.src)** `#intermediario` `#volume` `#trending`

#### Price Action Essenciais
- **[PhiCube_PrecoTempo](estrategias/exemplos/editaveis/automations/reversao_a_media/PhiCube_PrecoTempo.src)** `#avancado` `#price-action` `#multi-timeframe`
- **[Rainbow_Charts_4](estrategias/exemplos/editaveis/indicadores/tendencia/Rainbow_Charts_4.txt)** `#intermediario` `#moving-average` `#trending`

### 🎯 Filtros Rápidos por Uso

#### Para Iniciantes (`#iniciante`)
Busque por: `2MV_Padrao`, `DOISMV_padrao`, `Awesome_Oscillator`, `ROC`

#### Para Day Traders (`#day-trade`)
Busque por: `Larry_Williams`, `STORMER`, `Scalping`, `MACD_COLOR`

#### Para Swing Traders (`#swing`)
Busque por: `Bollinger`, `GridDinamico`, `Pisani`, `PhiCube`

#### Para Mercados Voláteis (`#volatile`)
Busque por: `Breakout`, `KASTR_SCALP`, `TTM_Squeeze`, `Volatility_Switch`

---

## Automações

### Cruzamento de Médias
- **[2MV_Padrao](estratégias/exemplos/editaveis/automations/cruzamento_de_medias/2MV_Padrao.txt)** `#iniciante` `#baixo-risco` `#moving-average` `#multi-timeframe`
  Esta automação executa ordens de compra e venda com base no cruzamento do preço de fechamento com uma média móvel exponencial de 20 períodos, aplicada às máximas e mínimas.
  * **Compra:** Entra comprado a mercado se o fechamento for maior que a MME de 20 períodos da máxima.
  * **Venda:** Entra vendido a mercado se o fechamento for menor que a MME de 20 períodos da mínima.
  * **Saída:** Zera a posição comprada se o fechamento cruzar para baixo da MME de 20 da mínima, e zera a posição vendida se o fechamento cruzar para cima da MME de 20 da máxima.
  * **Gerenciamento:** Não possui gerenciamento de risco explícito (gain/loss).

- **[__ESTRUTURA__PARCIAL](estratégias/exemplos/editaveis/automations/cruzamento_de_medias/__ESTRUTURA__PARCIAL.txt)** `#intermediario` `#moving-average` `#selective`
  Template de uma estratégia de cruzamento de médias com lógica para saídas parciais e stop. A condição de entrada é um cruzamento de médias.

- **[__TESTE_COMPRA_1M](estratégias/exemplos/editaveis/automations/cruzamento_de_medias/__TESTE_COMPRA_1M.txt)** `#iniciante` `#moving-average` `#intraday`
  Estratégia simples que compra no cruzamento de uma média e tem uma saída baseada em tempo (`CalcTime`).

- **[DOISMV_padrao](estratégias/exemplos/editaveis/automations/cruzamento_de_medias/DOISMV_padrao.txt)** `#iniciante` `#baixo-risco` `#moving-average` `#multi-timeframe`
  Cópia do script `2MV_Padrao.txt`.

- **[EXEC_CRUZAMENTO_DE_MEDIAS](estratégias/exemplos/editaveis/automations/cruzamento_de_medias/EXEC_CRUZAMENTO_DE_MEDIAS.txt)** `#iniciante` `#moving-average` `#multi-timeframe`
  Estratégia simples de cruzamento de médias móveis.

- **[RAMPA_DE_CAIXA](estratégias/exemplos/editaveis/automations/cruzamento_de_medias/RAMPA_DE_CAIXA.txt)** `#intermediario` `#moving-average` `#trending`
  Automação baseada no cruzamento de médias móveis, com gerenciamento de saídas parciais e stop.

### Price Action
- **[_COR_TESTE](estratégias/exemplos/editaveis/automations/price_action/_COR_TESTE.txt)** `#iniciante` `#price-action` `#intraday`
  Estratégia de teste que entra com `BuyStop` baseado em um padrão de candle específico.

- **[_EXEC_TRAP_DE_COMPRA](estratégias/exemplos/editaveis/automations/price_action/_EXEC_TRAP_DE_COMPRA.txt)** `#intermediario` `#price-action` `#day-trade` `#volatile`
  Estratégia do tipo 'armadilha' (trap). Posiciona uma ordem de compra (`BuyStop`) na máxima de um candle que violinou a mínima do dia anterior.

- **[_stormer_trap_close_max_mini](estratégias/exemplos/editaveis/automations/price_action/_stormer_trap_close_max_mini.txt)** `#avancado` `#price-action` `#day-trade` `#volatile`
  Estratégia de trap que busca por padrões de rompimento falso da máxima/mínima do dia anterior para entrar na operação.

- **[CACA_TOPO](estratégias/exemplos/editaveis/automations/price_action/CACA_TOPO.txt)** `#intermediario` `#price-action` `#day-trade` `#selective`
  Estratégia que busca por padrões de topo para entrar vendido no mercado.

- **[CACADOR_DE_FUNDOS](estratégias/exemplos/editaveis/automations/price_action/CACADOR_DE_FUNDOS.txt)** `#intermediario` `#price-action` `#day-trade` `#selective`
  Estratégia que busca por padrões de fundo para entrar comprado no mercado.

- **[STP0003_Trade_e_Acoes_Setup_Larry_Williams_Classico](estrategias/exemplos/editaveis/automations/price_action/STP0003_Trade_e_Acoes_Setup_Larry_Williams_Classico.txt)** `#intermediario` `#day-trade` `#price-action` `#moving-average`
  Estratégia de Larry Williams que opera rompimentos de mínimas/máximas com base na direção de uma média móvel de 20 períodos.

- **[STP0004_Indicador_Trade_E_Acoes_PFR](estrategias/exemplos/editaveis/indicadores/price_action/STP0004_Indicador_Trade_E_Acoes_PFR.txt)**
  Regra de coloração que pinta os candles de azul se o preço de fechamento for maior que o anterior e a mínima for menor que as duas mínimas anteriores, ou cinza se o fechamento for menor que o anterior e a máxima for maior que as duas máximas anteriores.

- **[STP0011_Trade_e_Acoes_Regra_de_Coloracao_Inside_Bar](estrategias/exemplos/editaveis/indicadores/price_action/STP0011_Trade_e_Acoes_Regra_de_Coloracao_Inside_Bar.txt)**
  Regra de coloração que pinta os candles de azul quando um padrão de Inside Bar é identificado.

- **[TopoFundo](estrategias/exemplos/editaveis/indicadores/price_action/TopoFundo.src)**
  Indicador que detecta e plota topos e fundos com base em um período definido.

- **[V0003_VENOFIBOPOITS](estrategias/exemplos/editaveis/indicadores/price_action/V0003_VENOFIBOPOITS.txt)**
  Indicador que plota linhas de Fibonacci baseadas no ajuste anterior.

- **[V0005_OpenVNZ_cote](estrategias/exemplos/editaveis/indicadores/price_action/V0005_OpenVNZ_cote.txt)**
  Indicador que plota a abertura do dia atual e anterior, mínima do dia anterior e ajuste.
- **[STP0005_Trade_e_Acoes_Setup_InsideBar](estrategias/exemplos/editaveis/automations/price_action/STP0005_Trade_e_Acoes_Setup_InsideBar.txt)** `#intermediario` `#price-action` `#swing` `#baixo-risco`
  Estratégia que opera o rompimento de Inside Bars, com gerenciamento de stop gain e stop loss.

- **[STP0006_Trade_e_Acoes_Setup_9_1_Larry_Wiilians](estrategias/exemplos/editaveis/automations/price_action/STP0006_Trade_e_Acoes_Setup_9_1_Larry_Wiilians.txt)** `#avancado` `#day-trade` `#price-action` `#moving-average`
  Estratégia de Larry Williams (Setup 9.1) que opera rompimentos de máximas/mínimas com base em médias móveis, incluindo gerenciamento de risco.

- **[STP0007_Trade_e_Acoes_Setup_Media_Movel_9_Larry_Wiilians](estrategias/exemplos/editaveis/automations/price_action/STP0007_Trade_e_Acoes_Setup_Media_Movel_9_Larry_Wiilians.txt)** `#intermediario` `#day-trade` `#moving-average` `#trending`
  Estratégia de Larry Williams (Setup Média Móvel 9) que opera cruzamentos de médias móveis para entrada e saída de posições.

- **[STP0008_Trade_e_Acoes_Setup_Davy_Landry_Swing_Trade](estrategias/exemplos/editaveis/automations/price_action/STP0008_Trade_e_Acoes_Setup_Davy_Landry_Swing_Trade.txt)** `#avancado` `#swing` `#price-action` `#moving-average`
  Estratégia de Swing Trade baseada no setup de Dave Landry, que busca por padrões de price action e médias móveis para entradas.

- **[V0045_Setup_Primeira_Barra](estrategias/exemplos/editaveis/automations/price_action/V0045_Setup_Primeira_Barra.txt)** `#intermediario` `#intraday` `#price-action` `#selective`
  Estratégia que opera o rompimento da primeira barra do dia, com stop gain e stop loss definidos.

### Reversão à Média
- **[1PTV](estratégias/exemplos/editaveis/automations/reversao_a_media/1PTV.txt)** `#avancado` `#swing` `#volatile` `#volume`
  Estratégia complexa que parece operar com base em diferenciais calculados a partir do volume e da volatilidade do candle. A lógica de entrada é ofuscada e baseada na comparação de 4 variáveis (`diffVal1` a `diffVal4`) que não são claramente definidas, tornando a intenção exata difícil de decifrar sem mais contexto.
  * **Compra:** `BuyAtMarket` quando `diffVal2 <= diffVal1`.
  * **Venda:** `SellShortAtMarket` quando `diffVal3 <= diffVal2`.
  * **Gerenciamento:** Utiliza variáveis de controle (`boughtAtMarket`, `soldAtMarket`) para evitar entradas consecutivas, mas não possui stops de ganho ou perda definidos.

- **[__ESTRATEGIA_VENCEDORA](estratégias/exemplos/editaveis/automations/reversao_a_media/__ESTRATEGIA_VENCEDORA.txt)** `#intermediario` `#sideways` `#bollinger` `#selective`
  Estratégia que opera reversão à média usando Bandas de Bollinger e Estocástico. Compra em sobre-venda na banda inferior e vende em sobre-compra na banda superior.

- **[__EXEC_COMPRA6MI_10PT](estratégias/exemplos/editaveis/automations/reversao_a_media/__EXEC_COMPRA6MI_10PT.txt)** `#intermediario` `#intraday` `#rsi` `#high-frequency`
  Estratégia de scalping que compra quando o `RsiStochastic` cruza para cima de zero e sai com alvo fixo de pontos ou por tempo.

- **[__EXECUCAO_RETORNO_A_MEDIA](estratégias/exemplos/editaveis/automations/reversao_a_media/__EXECUCAO_RETORNO_A_MEDIA.txt)** `#iniciante` `#sideways` `#moving-average` `#baixo-risco`
  Robô que opera o retorno à média. Compra quando o preço cruza uma MME para cima após ter se afastado para baixo, e vice-versa.

- **[_EXEC_CANAL_KELTNER](estratégias/exemplos/editaveis/automations/reversao_a_media/_EXEC_CANAL_KELTNER.txt)** `#intermediario` `#sideways` `#selective` `#volatile`
  Opera a reversão à média nos Canais de Keltner, comprando abaixo do canal e vendendo para zerar acima.

- **[_EXEC_MAXIMO_MINIMO](estratégias/exemplos/editaveis/automations/reversao_a_media/_EXEC_MAXIMO_MINIMO.txt)** `#iniciante` `#sideways` `#rsi` `#selective`
  Estratégia que compra em níveis de sobrevenda do RSI e sai da operação após um número fixo de candles.

- **[_RETORNO_MEDIA](estratégias/exemplos/editaveis/automations/reversao_a_media/_RETORNO_MEDIA.txt)** `#iniciante` `#sideways` `#moving-average` `#baixo-risco`
  Cópia da estratégia `__EXECUCAO_RETORNO_A_MEDIA`.

- **[BollingerBuyer](estratégias/exemplos/editaveis/automations/reversao_a_media/BollingerBuyer.txt)** `#iniciante` `#sideways` `#bollinger` `#baixo-risco`
  Estratégia que compra na banda inferior de Bollinger e vende na banda superior.

- **[COMPRA_BBANDS](estratégias/exemplos/editaveis/automations/reversao_a_media/COMPRA_BBANDS.txt)** `#intermediario` `#sideways` `#bollinger` `#volume`
  Estratégia que compra/vende com base em Bandas de Bollinger, volume e Estocástico, incluindo gerenciamento de ganho/perda e saída por tempo.

- **[WDO_Leilao](estratégias/exemplos/editaveis/automations/reversao_a_media/WDO_Leilao.txt)** `#intermediario` `#sideways` `#bollinger` `#alto-retorno`
  Estratégia de reversão à média que opera com base nas Bandas de Bollinger.
  * **Compra:** Entra comprado a mercado quando o preço está abaixo da banda inferior.
  * **Venda:** Entra vendido a mercado quando o preço está acima da banda superior.
  * **Gerenciamento:** Aumenta a posição se o preço se move contra a posição inicial e sai da operação com lucro, quando o preço retorna à média.

- **[Pisani_Stocastic](estratégias/exemplos/editaveis/automations/reversao_a_media/Pisani_Stocastic.txt)** `#avancado` `#swing` `#baixo-risco` `#selective`
  Estratégia baseada em Bandas Pisani, VWAP Bands, RSI e médias móveis, com gerenciamento de risco detalhado.

- **[STP0009_Trade_e_Acoes_Setup_Stocastico_Lento](estrategias/exemplos/editaveis/automations/reversao_a_media/STP0009_Trade_e_Acoes_Setup_Stocastico_Lento.txt)** `#intermediario` `#sideways` `#selective` `#baixo-risco`
  Estratégia que opera a reversão à média utilizando o oscilador Estocástico Lento, comprando em sobrevenda e vendendo em sobrecompra.

- **[V0046_Estrategia_IFR2](estrategias/exemplos/editaveis/automations/reversao_a_media/V0046_Estrategia_IFR2.txt)** `#intermediario` `#sideways` `#rsi` `#selective`
  Estratégia que compra quando o RSI de 2 períodos atinge níveis de sobrevenda e gerencia a saída com stop móvel ou por tempo.

### Rompimento
- **[___SETUP_ESTRATEGICO - Copia](estratégias/exemplos/editaveis/automations/rompimento/___SETUP_ESTRATEGICO - Copia.txt)** `#avancado` `#trending` `#moving-average` `#selective`
  Estratégia de rompimento que entra com ordens `BuyStop` e `SellShortStop` baseadas em condições de cruzamento de médias. Inclui lógica para saídas parciais e stop.

- **[___SETUP_ESTRATEGICO](estratégias/exemplos/editaveis/automations/rompimento/___SETUP_ESTRATEGICO.txt)** `#avancado` `#trending` `#moving-average` `#selective`
  Versão principal da estratégia de rompimento acima.

- **[__EX_BOLINGER_BANDS](estratégias/exemplos/editaveis/automations/rompimento/__EX_BOLINGER_BANDS.txt)** `#intermediario` `#volatile` `#bollinger` `#trending`
  Estratégia de rompimento que compra quando o preço fecha acima da Banda de Bollinger superior e vende quando fecha abaixo da inferior.

- **[__EX_COMPRA_NA_ALTA](estratégias/exemplos/editaveis/automations/rompimento/__EX_COMPRA_NA_ALTA.txt)** `#iniciante` `#trending` `#price-action` `#moving-average`
  Estratégia simples que posiciona uma ordem de compra (`BuyStop`) na máxima de um candle que atende a certas condições de price action e média.

- **[_estratgiamatadora](estratégias/exemplos/editaveis/automations/rompimento/_estratgiamatadora.txt)** `#intermediario` `#volatile` `#bollinger` `#alto-retorno`
  É uma cópia da estratégia `BollingerBreakout`, que opera o rompimento das Bandas de Bollinger.

- **[_ESTRUTURA_PARCIAL_EXECUCAO](estratégias/exemplos/editaveis/automations/rompimento/_ESTRUTURA_PARCIAL_EXECUCAO.txt)** `#intermediario` `#price-action` `#selective` `#trending`
  Template de uma estratégia de rompimento de inside bar, com lógica para saídas parciais.

- **[_EXEC_BollingerBreakoutBETA](estratégias/exemplos/editaveis/automations/rompimento/_EXEC_BollingerBreakoutBETA.txt)** `#intermediario` `#volatile` `#bollinger` `#baixo-risco`
  Estratégia de rompimento de Bandas de Bollinger com stop loss percentual.

- **[Alta e Baixa](estratégias/exemplos/editaveis/automations/rompimento/Alta e Baixa.txt)** `#iniciante` `#trending` `#price-action` `#multi-timeframe`
  Estratégia que compra no rompimento da máxima dos últimos 10 candles e vende no rompimento da mínima. Inclui stop e alvo fixos.

- **[BollingerBreakout](estratégias/exemplos/editaveis/automations/rompimento/BollingerBreakout.txt)** `#intermediario` `#volatile` `#bollinger` `#alto-retorno`
  Estratégia clássica que opera o rompimento das Bandas de Bollinger.

### Scalping
- **[__KASTR_SCALP_12R](estratégias/exemplos/editaveis/automations/scalping/__KASTR_SCALP_12R.txt)** `#avancado` `#intraday` `#high-frequency` `#volatile`
  Estratégia de scalping para Renko (12R) com lógica de entrada complexa baseada em padrões de candles e IFR. Saídas com alvo e stop fixos.

### Seguidor de Tendência
- **[_COR_MILIONARIO_7R](estratégias/exemplos/editaveis/automations/seguidor_de_tendencia/_COR_MILIONARIO_7R.txt)** `#avancado` `#trending` `#moving-average` `#alto-retorno`
  Estratégia para Renko (7R) que entra no mercado com base em sinais do `ADAPTIVEMOVINGAVERAGE` e `TopBottomDetector`.

- **[__EXEC_ADX_DIDI](estratégias/exemplos/editaveis/automations/seguidor_de_tendencia/__EXEC_ADX_DIDI.txt)** `#intermediario` `#trending` `#selective` `#multi-timeframe`
  Robô que opera comprado baseado no cruzamento do DI+ sobre o DI- e na direção do Didi Index, com um stop de tempo.

- **[_EXEC_VIRADA_HILOW](estratégias/exemplos/editaveis/automations/seguidor_de_tendencia/_EXEC_VIRADA_HILOW.txt)** `#intermediario` `#trending` `#selective` `#multi-timeframe`
  Estratégia que segue a tendência indicada pelo HiLo Activator, comprando na virada para alta e vendendo na virada para baixa.

- **[_HILOW_ESTRATEGIA](estratégias/exemplos/editaveis/automations/seguidor_de_tendencia/_HILOW_ESTRATEGIA.txt)** `#intermediario` `#trending` `#volume` `#selective`
  Estratégia que entra a favor da tendência do HiLo Activator, com um filtro de volume e uma saída por tempo.

- **[ESTRATEGADOADXCOMDIDI](estratégias/exemplos/editaveis/automations/seguidor_de_tendencia/ESTRATEGADOADXCOMDIDI.txt)** `#avancado` `#trending` `#multi-timeframe` `#selective`
  Estratégia que combina ADX, Didi Index e CCI para sinais de entrada e saída.

- **[HILO_Renko](estratégias/exemplos/editaveis/automations/seguidor_de_tendencia/HILO_Renko.txt)** `#intermediario` `#trending` `#selective` `#multi-timeframe`
  Estratégia para Renko que opera seguindo a tendência do indicador HiLo Activator.

- **[MILIONARIO_RENKO](estratégias/exemplos/editaveis/automations/seguidor_de_tendencia/MILIONARIO_RENKO.txt)** `#avancado` `#trending` `#alto-retorno` `#moving-average`
  Automação para Renko que opera seguindo a tendência com base em médias e no detector de topos/fundos.

### Tendência
- **[compra_tilso](estratégias/exemplos/editaveis/automations/tendencia/compra_tilso.txt)** `#intermediario` `#trending` `#moving-average` `#selective`
  Estratégia que compra/vende com base no indicador Tilson e uma média móvel.

- **[V0053_Exec_VmaSimple_1.0](estrategias/exemplos/editaveis/automations/tendencia/V0053_Exec_VmaSimple_1.0.txt)** `#intermediario` `#trending` `#moving-average` `#multi-timeframe`
  Estratégia de execução que utiliza uma VMA (Média Móvel Variável) como base para entradas e saídas, com gerenciamento de posição.

### Diversos
- **[santoGraao](estrategias/exemplos/editaveis/automations/diversos/santoGraao.txt)** `#intermediario` `#price-action` `#rsi` `#selective`
  Estratégia que combina detecção de topos/fundos e IFR para sinais de compra e venda.

- **[V0049_TIQUIM_2_0Revisado](estrategias/exemplos/editaveis/automations/diversos/V0049_TIQUIM_2_0Revisado.txt)** `#avancado` `#multi-timeframe` `#bollinger` `#rsi`
  Estratégia de negociação que utiliza Hilo Activator, Bandas de Bollinger, IFR e médias móveis para sinais de entrada e saída, com gerenciamento de risco.

- **[V0056_60_alarme](estrategias/exemplos/editaveis/automations/diversos/V0056_60_alarme.txt)** `#intermediario` `#volume` `#intraday` `#selective`
  Indicador que gera sinais de alarme baseados em agressão de volume e range, com condições de preço.

---

## Indicadores

### Outros
- **[__CONTA_VELAS](estratégias/exemplos/editaveis/indicadores/outros/__CONTA_VELAS.txt)**
  Um contador simples que plota o número de barras (candles) desde o início do dia.

- **[_DOIS_PLOTS](estratégias/exemplos/editaveis/indicadores/outros/_DOIS_PLOTS.txt)**
  Script genérico que plota duas fontes de dados quaisquer, por padrão a abertura e o fechamento.

- **[Autor](estratégias/exemplos/editaveis/indicadores/outros/Autor.txt)**
  Arquivo de texto com um link para um gist no GitHub.

- **[Better_Volume_Original](estratégias/exemplos/editaveis/indicadores/outros/Better_Volume_Original.txt)**
  Arquivo de texto com a descrição e códigos em outras linguagens do indicador 'Better Volume'.

- **[BLOCO_MESTRE_SCRIPT](estratégias/exemplos/editaveis/indicadores/outros/BLOCO_MESTRE_SCRIPT.txt)**
  Arquivo de texto que serve como um template, explicando a estrutura de um script NTSL.

- **[Candle_Variation_Percentage](estratégias/exemplos/editaveis/indicadores/outros/Candle_Variation_Percentage.txt)**
  Calcula e plota a variação percentual do candle (fechamento vs. abertura).

- **[Curva_Curta_Juros](estratégias/exemplos/editaveis/indicadores/outros/Curva_Curta_Juros.txt)**
  Plota a variação de diversos ativos (WIN, WDO, DI, PETR4, VALE3) e suas médias móveis.

- **[Dias](estratégias/exemplos/editaveis/indicadores/outros/Dias.txt)**
  Um filtro simples que permite plotar dados apenas a partir de um certo número de dias anteriores.

- **[Failed](estratégias/exemplos/editaveis/indicadores/outros/Failed.txt)**
  Script incompleto que parece calcular métricas baseadas em volume.

- **[Conta_Barras](estratégias/exemplos/editaveis/indicadores/outros/Conta_Barras.src)**
  Conta e plota o número de barras desde a última mudança de data.

- **[Conta_Barras_Intraday](estratégias/exemplos/editaveis/indicadores/outros/Conta_Barras_Intraday.src)**
  Conta e plota o número de barras dentro do dia de negociação atual.

  - **[IFR_gator](estratégias/exemplos/editaveis/indicadores/outros/IFR_gator.txt)**
  Arquivo de texto com a descrição e códigos em outras linguagens do indicador 'IFR Gator'.

- **[Linha_Guia_de_Renko](estratégias/exemplos/editaveis/indicadores/outros/Linha_Guia_de_Renko.txt)**
  Arquivo de texto com a descrição de um indicador para Renko.

- **[Max](estratégias/exemplos/editaveis/indicadores/outros/Max.txt)**
  Plota o valor máximo entre duas fontes de dados.
- **[Scalping](estratégias/exemplos/editaveis/indicadores/outros/Scalping)**
  Regra de coloração que pinta os candles de acordo com a direção do preço em relação ao candle anterior e a duração da barra.
- **[Setup_Larry](estratégias/exemplos/editaveis/indicadores/outros/Setup_Larry.txt)**
  Regra de coloração que identifica padrões de setup de Larry Williams (Ponto Contínuo, 9.1, 9.2, 9.3) e pinta os candles de acordo.

- **[unknownfile](estrategias/exemplos/editaveis/indicadores/outros/unknownfile)**
  Arquivo com conteúdo truncado, mas que parece ser um indicador relacionado a cálculos de preço e volume.

- **[V0055_TEST_ARRAY](estrategias/exemplos/editaveis/indicadores/outros/V0055_TEST_ARRAY.txt)**
  Script de teste para demonstração de uso de arrays.

- **[IFR_gator](estratégias/exemplos/editaveis/indicadores/outros/IFR_gator.txt)**
  Arquivo de texto com a descrição e códigos em outras linguagens do indicador 'IFR Gator'.

### Osciladores
- **[__EM_ESTUDO](estratégias/exemplos/editaveis/indicadores/osciladores/__EM_ESTUDO.txt)**
  Script experimental e incompleto para o cálculo do RVI (Relative Vigor Index).

- **[__TESTE_PLOTS_ENTRADAS](estratégias/exemplos/editaveis/indicadores/osciladores/__TESTE_PLOTS_ENTRADAS.txt)**
  Plota pontos de entrada e saída com base em condições de sobrecompra/venda do Estocástico e IFR.

- **[_Didi_Exp](estratégias/exemplos/editaveis/indicadores/osciladores/_Didi_Exp.txt)**
  Uma variação do Didi Index que utiliza médias móveis exponenciais em seu cálculo.

- **[_Didi_F_i](estratégias/exemplos/editaveis/indicadores/osciladores/_Didi_F_i.txt)**
  Uma variação do Didi Index que utiliza o `ForceIndex` como dado de entrada, medindo a força do movimento.

- **[_Didi_hull](estratégias/exemplos/editaveis/indicadores/osciladores/_Didi_hull.txt)**
  Uma variação do Didi Index que utiliza a Média Móvel de Hull, que possui menos lag.

- **[_Didi_Momentum](estratégias/exemplos/editaveis/indicadores/osciladores/_Didi_Momentum.txt)**
  Uma variação do Didi Index que utiliza o indicador `Momentum` como dado de entrada.

- **[_Didi_Weis](estratégias/exemplos/editaveis/indicadores/osciladores/_Didi_Weis.txt)**
  Uma variação exótica do Didi Index que usa dados da Nuvem de Ichimoku em seu cálculo.

- **[_DIDIINDEX](estratégias/exemplos/editaveis/indicadores/osciladores/_DIDIINDEX.txt)**
  Plota as três linhas do indicador Didi Index padrão.

- **[_IFR_Didi](estratégias/exemplos/editaveis/indicadores/osciladores/_IFR_Didi.txt)**
  Variação do Didi Index que usa o IFR (RSI) como base para seus cálculos.

- **[_MEDIAS_IFR](estratégias/exemplos/editaveis/indicadores/osciladores/_MEDIAS_IFR.txt)**
  Plota médias móveis aplicadas sobre o IFR (RSI), suavizando o oscilador.

- **[MovROC](estratégias/exemplos/editaveis/indicadores/osciladores/MovROC.txt)**
  Indicador composto que agrega o sinal de 4 ROCs (Rate of Change) de diferentes períodos para gerar um único oscilador de momento.

- **[NIVEIS_DO_RSI](estratégias/exemplos/editaveis/indicadores/osciladores/NIVEIS_DO_RSI.txt)**
  Plota os níveis de máxima e mínima do RSI.

- **[PZO](estratégias/exemplos/editaveis/indicadores/osciladores/PZO.txt)**
  Plota o Volume Zone Oscillator (PZO).

- **[_ROC_RateOfChange](estratégias/exemplos/editaveis/indicadores/osciladores/_ROC_RateOfChange.txt)**
  Indicador clássico 'Rate of Change' que mede a variação percentual do preço.

- **[Alert_Compra_Venda](estratégias/exemplos/editaveis/indicadores/osciladores/Alert_Compra_Venda.txt)**
  Gera alertas quando o IFR (RSI) atinge níveis de sobrecompra (70) ou sobrevenda (30).

- **[Apirine_Slow_RSI](estratégias/exemplos/editaveis/indicadores/osciladores/Apirine_Slow_RSI.txt)**
  Uma variação do IFR (RSI) com suavização adicional.

- **[Awesome_Oscillator](estratégias/exemplos/editaveis/indicadores/osciladores/Awesome_Oscillator.txt)**
  Implementação padrão do Oscilador Incrível (Awesome Oscillator) de Bill Williams.

- **[BBstops-stochastic](estratégias/exemplos/editaveis/indicadores/osciladores/BBstops-stochastic.txt)**
  Plota níveis de stop loss baseados em Bandas de Bollinger aplicadas ao oscilador Estocástico.

- **[Buy_Sell_sign](estratégias/exemplos/editaveis/indicadores/osciladores/Buy_Sell_sign.txt)**
  Plota um oscilador similar ao Awesome Oscillator e colore as barras com base na sua direção.

- **[Buy_Sell_Signals](estratégias/exemplos/editaveis/indicadores/osciladores/Buy_Sell_Signals.txt)**
  Script incompleto que parece configurar sinais baseados no IFR (RSI).

- **[Connors_RSI](estratégias/exemplos/editaveis/indicadores/osciladores/Connors_RSI.txt)**
  Implementação do Connors RSI, um oscilador de momento composto.

- **[Derivative_Oscillator](estratégias/exemplos/editaveis/indicadores/osciladores/Derivative_Oscillator.txt)**
  Plota um 'Oscilador Derivativo', que é um MACD suavizado do IFR (RSI).

- **[DETECTA_TOPO_ESTOCASTICO](estratégias/exemplos/editaveis/indicadores/osciladores/DETECTA_TOPO_ESTOCASTICO.txt)**
  Plota níveis de máxima/mínima com base em um oscilador Estocástico transformado e colore as barras.

- **[DIDI_Index](estratégias/exemplos/editaveis/indicadores/osciladores/DIDI_Index.txt)**
  Plota o Didi Index (diferença entre médias móveis curtas, médias e longas).

- **[didi](estratégias/exemplos/editaveis/indicadores/osciladores/didi.txt)**
  Gera um alerta com base nas condições do ADX, Didi Index e CCI.

- **[Double_Laguerre](estratégias/exemplos/editaveis/indicadores/osciladores/Double_Laguerre.txt)**
  Plota dois indicadores Laguerre RSI com parâmetros diferentes e colore as barras com base no seu cruzamento.

- **[Dual_Stochastic](estratégias/exemplos/editaveis/indicadores/osciladores/Dual_Stochastic.txt)**
  Regra de coloração complexa baseada em dois osciladores Estocásticos (rápido e lento) e médias móveis.

- **[Exaustão_DOL_2R](estratégias/exemplos/editaveis/indicadores/osciladores/Exaustão_DOL_2R.txt)**
  Indicador complexo que combina IFR (RSI), MACD e outros elementos para detectar padrões de 'exaustão'.

- **[Fisher_Transform](estratégias/exemplos/editaveis/indicadores/osciladores/Fisher_Transform.src)**
  Implementação do indicador Fisher Transform de John Ehlers.

- **[Laguerre_PPO_PercentileRank](estratégias/exemplos/editaveis/indicadores/osciladores/Laguerre_PPO_PercentileRank.txt)**
  Implementação do Laguerre PPO com ranking de percentil.

- **[LRSI_MIRROR](estratégias/exemplos/editaveis/indicadores/osciladores/LRSI_MIRROR.txt)**
  Implementação do Laguerre RSI espelhado.

- **[MACD_COLOR2](estratégias/exemplos/editaveis/indicadores/osciladores/MACD_COLOR2.txt)**
  Regra de coloração baseada no cruzamento das linhas do MACD.

- **[IFR_Power](estratégias/exemplos/editaveis/indicadores/osciladores/IFR_Power.txt)**
  Regra de coloração que mede a força da tendência com base no IFR (RSI) e no OBV.

- **[LZ_IFR2](estratégias/exemplos/editaveis/indicadores/osciladores/LZ_IFR2.txt)**
  Plota médias exponenciais do IFR (RSI) para gerar sinais de oscilador.

- **[LZ_IFR2-2](estratégias/exemplos/editaveis/indicadores/osciladores/LZ_IFR2-2.txt)**
  Indicador que plota e colore as barras com base em médias do IFR e no MACD do IFR.

- **[MACD_CorDeGatilho_v2](estratégias/exemplos/editaveis/indicadores/osciladores/MACD_CorDeGatilho_v2.txt)**
  Indicador que usa o MACD e uma média de gatilho para colorir as barras.

- **[MACDTeste](estratégias/exemplos/editaveis/indicadores/osciladores/MACDTeste.txt)**
  Variação do MACD que plota e colore as barras com base na diferença entre a linha do MACD e sua linha de sinal.

- **[Simple_Harmonic_Oscillator](estrategias/exemplos/editaveis/indicadores/osciladores/Simple_Harmonic_Oscillator)**
  Implementação do oscilador harmônico simples (SHO), que mede a relação entre o preço e sua média móvel.

- **[V0009_VenoM_oscilator_Range](estrategias/exemplos/editaveis/indicadores/osciladores/V0009_VenoM_oscilator_Range.txt)**
  Indicador que plota a oscilação de médias entre dois níveis, útil para identificar zonas de sobrecompra/sobrevenda.

- **[V0012_VNZ_RSI_Slow](estrategias/exemplos/editaveis/indicadores/osciladores/V0012_VNZ_RSI_Slow.txt)**
  Indicador que plota uma média entre o RSI e uma média móvel, funcionando como um oscilador.

- **[V0028_WaveTrend_Oscillator](estrategias/exemplos/editaveis/indicadores/osciladores/V0028_WaveTrend_Oscillator.txt)**
  Indicador que plota um oscilador de tendência de onda.

- **[V0037_zCCI_IFR](estrategias/exemplos/editaveis/indicadores/osciladores/V0037_zCCI_IFR.txt)**
  Indicador que compara o RSI com o CCI de diferentes escalas de fator.

- **[V0040_TTM_Squeeze](estrategias/exemplos/editaveis/indicadores/osciladores/V0040_TTM_Squeeze.txt)**
  Indicador que plota o oscilador TTM Squeeze, que mede a volatilidade e o momento do mercado.

- **[V0042_Triple_TRIX](estrategias/exemplos/editaveis/indicadores/osciladores/V0042_Triple_TRIX.txt)**
  Indicador que plota três linhas do indicador TRIX com diferentes períodos.

- **[V0060_Superpassband](estrategias/exemplos/editaveis/indicadores/osciladores/V0060_Superpassband.txt)**
  Indicador que plota um filtro passa-banda e colore os candles de acordo com a posição do preço em relação a ele.

### Price Action
- **[___ZFIBOPointControl](estratégias/exemplos/editaveis/indicadores/price_action/___ZFIBOPointControl.txt)**
  Plota níveis de Fibonacci (retração ou projeção) baseados no preço de fechamento do dia anterior (`PriorCote`).

- **[__ABERTURA_DIA_RENKO](estratégias/exemplos/editaveis/indicadores/price_action/__ABERTURA_DIA_RENKO.txt)**
  Desenvolvido para Renko, plota a abertura do dia e colore os candles de azul (acima) ou vermelho (abaixo).

- **[__AJUSTE_DIAS_ANTERIORES](estratégias/exemplos/editaveis/indicadores/price_action/__AJUSTE_DIAS_ANTERIORES.txt)**
  Plota o preço de ajuste (`PriorCote(4)`) de dias anteriores como linhas de suporte/resistência.

- **[__COR_COMPRA_VENDE](estratégias/exemplos/editaveis/indicadores/price_action/__COR_COMPRA_VENDE.txt)**
  Regra de coloração que pinta os candles de azul ou fúcsia com base em padrões de price action simples, comparando a posição do candle atual com o anterior.

- **[__DE_HORA_EM_HORA](estratégias/exemplos/editaveis/indicadores/price_action/__DE_HORA_EM_HORA.txt)**
  Plota uma linha horizontal na máxima do primeiro candle de cada hora, servindo como um nível de referência intradiário.

- **[__DETECTOR_TOPO_FUNDO](estratégias/exemplos/editaveis/indicadores/price_action/__DETECTOR_TOPO_FUNDO.txt)**
  Indicador que plota linhas horizontais em topos e fundos detectados automaticamente, que persistem no gráfico por um tempo.

- **[__ESTUDO_TOPOS_AUTOATICO](estratégias/exemplos/editaveis/indicadores/price_action/__ESTUDO_TOPOS_AUTOATICO.txt)**
  Plota linhas de suporte e resistência baseadas nas máximas e mínimas do dia (`HighD`, `LowD`).

- **[__INDICADOR_GAP](estratégias/exemplos/editaveis/indicadores/price_action/__INDICADOR_GAP.txt)**
  Detecta gaps de abertura (acima de um `tamanho_do_gap` definido) e plota uma linha no preço de abertura, colorindo o candle do gap.

- **[__MAX_INSIDE_CANDLE](estratégias/exemplos/editaveis/indicadores/price_action/__MAX_INSIDE_CANDLE.txt)**
  Detecta o padrão de candle 'Inside Bar' (candle contido pelo anterior) e plota seu range (máxima, mínima e meio).

- **[__MAXIMAS_EMINIMAS_DE_60](estratégias/exemplos/editaveis/indicadores/price_action/__MAXIMAS_EMINIMAS_DE_60.txt)**
  Plota a máxima e a mínima da primeira hora de negociação como linhas de suporte e resistência para o resto do dia.

- **[__PROJECAO_DE_FIBONACCI](estratégias/exemplos/editaveis/indicadores/price_action/__PROJECAO_DE_FIBONACCI.txt)**
  Plota projeções de Fibonacci (níveis percentuais) a partir do preço de abertura do dia.

- **[__ROBO_FIBONACCI](estratégias/exemplos/editaveis/indicadores/price_action/__ROBO_FIBONACCI.txt)**
  Desenha retrações de Fibonacci automaticamente entre os topos e fundos mais recentes detectados pela função `TopBottomDetector`.

- **[_999](estratégias/exemplos/editaveis/indicadores/price_action/_999.txt)**
  Indicador que busca por um padrão de fundo em 'W' (quatro candles fazendo um fundo duplo) e plota uma linha no nível do fundo encontrado.

- **[_AJUSTES_ANTERIORES](estratégias/exemplos/editaveis/indicadores/price_action/_AJUSTES_ANTERIORES.txt)**
  Plota os preços de ajuste de dias anteriores, junto com níveis percentuais (Fibonacci) baseados no fechamento do dia anterior.

- **[_DETECTOR_DETOPOS](estratégias/exemplos/editaveis/indicadores/price_action/_DETECTOR_DETOPOS.txt)**
  Utiliza `TopBottomDetector` para identificar e plotar topos no gráfico.

- **[_IND_ABERTURDODIA](estratégias/exemplos/editaveis/indicadores/price_action/_IND_ABERTURDODIA.txt)**
  Plota o preço de abertura do dia.

- **[_IND_NIVEIS_PERCENTUAIS](estratégias/exemplos/editaveis/indicadores/price_action/_IND_NIVEIS_PERCENTUAIS.txt)**
  Plota níveis percentuais (Fibonacci) acima e abaixo de um `PriorCote` (fechamento, ajuste, etc.).

- **[_IND_PRECO_ABERTURA](estratégias/exemplos/editaveis/indicadores/price_action/_IND_PRECO_ABERTURA.txt)**
  Plota níveis percentuais (Fibonacci) com base no preço de abertura do dia.

- **[_PRINCIPAIS_S_R](estratégias/exemplos/editaveis/indicadores/price_action/_PRINCIPAIS_S_R.txt)**
  Plota a máxima e a mínima do dia como linhas de suporte e resistência.

- **[_Prior_Cote_Abertura](estratégias/exemplos/editaveis/indicadores/price_action/_Prior_Cote_Abertura.txt)**
  Plota as aberturas dos 4 dias anteriores.

- **[_Prior_Cote_Fechamentos](estratégias/exemplos/editaveis/indicadores/price_action/_Prior_Cote_Fechamentos.txt)**
  Plota os fechamentos dos 4 dias anteriores.

- **[_Prior_Cote_Maxima](estratégias/exemplos/editaveis/indicadores/price_action/_Prior_Cote_Maxima.txt)**
  Plota as máximas dos 4 dias anteriores.

- **[_Prior_Cote_Minima](estratégias/exemplos/editaveis/indicadores/price_action/_Prior_Cote_Minima.txt)**
  Plota as mínimas dos 4 dias anteriores.

- **[_TOPO_FUNDO_MAGICO](estratégias/exemplos/editaveis/indicadores/price_action/_TOPO_FUNDO_MAGICO.txt)**

- **[gaps](estratégias/exemplos/editaveis/indicadores/price_action/gaps.src)**
  Detecta e colore gaps de abertura.

- **[padroes_candles](estratégias/exemplos/editaveis/indicadores/price_action/padroes_candles.src)**
  Colore as barras com base na identificação de diversos padrões de candlestick (Shooting Star, Hammer, Engulfing, Harami).

- **[PhiCube_PC_B2](estratégias/exemplos/editaveis/indicadores/price_action/PhiCube_PC_B2.src)**
  Plota níveis de preço calculados a partir de máximas e mínimas de períodos específicos, com base na metodologia PhiCube.

- **[PhiCube_PV_B2](estratégias/exemplos/editaveis/indicadores/price_action/PhiCube_PV_B2.src)**
  Plota níveis de preço calculados a partir de máximas e mínimas de períodos específicos, com base na metodologia PhiCube.

- **[Phicube_PCPV_0072](estratégias/exemplos/editaveis/indicadores/price_action/Phicube_PCPV_0072.txt)**
  Plota níveis de Fibonacci (PhiCube) baseados em máximas e mínimas de períodos.

- **[PhiCube_PCPV_Flexivel](estratégias/exemplos/editaveis/indicadores/price_action/PhiCube_PCPV_Flexivel.src)**
  Plota níveis de Fibonacci (PhiCube) de forma flexível, com base em períodos variáveis.

- **[Pivot_Plotagem_all](estratégias/exemplos/editaveis/indicadores/price_action/Pivot_Plotagem_all.src)**
  Calcula e plota diversos tipos de níveis de pivô (Floor, Demark, Woodie, Camarilla, Fibonacci).

- **[Pivot_ROMP](estratégias/exemplos/editaveis/indicadores/price_action/Pivot_ROMP.txt)**
  Colore as barras quando o preço rompe os níveis de pivô.

- **[Pivots_Basicos](estratégias/exemplos/editaveis/indicadores/price_action/Pivots_Basicos.src)**
  Calcula e plota os pivôs básicos (Floor Pivots).

- **[Quatro_Ajustes_anteriores](estratégias/exemplos/editaveis/indicadores/price_action/Quatro_Ajustes_anteriores.txt)**
  Plota os preços de ajuste de dias anteriores.
  Regra de coloração que pinta os candles de forma diferente dependendo da sequência de topos e fundos detectados.

- **[_TOPOS_FUDOS_AUTOMATICOS](estratégias/exemplos/editaveis/indicadores/price_action/_TOPOS_FUDOS_AUTOMATICOS.txt)**
  Plota linhas horizontais em topos e fundos detectados automaticamente no gráfico.

- **[_TOPOS_FUNDOS_IMPORTANTES](estratégias/exemplos/editaveis/indicadores/price_action/_TOPOS_FUNDOS_IMPORTANTES.txt)**
  Detecta e plota topos e fundos usando `TopBottomDetector` com diferentes periodicidades.

- **[ABERTURA_DEQUINZE](estratégias/exemplos/editaveis/indicadores/price_action/ABERTURA_DEQUINZE.txt)**
  Plota duas linhas horizontais: uma no nível da máxima do candle das 09:00 e outra no nível da máxima do candle das 09:15, mantendo-as no gráfico até as 18:30. Serve para marcar os níveis de preço da abertura do mercado.

- **[ABERTURDODIA](estratégias/exemplos/editaveis/indicadores/price_action/ABERTURDODIA.txt)**
  Plota o preço de abertura do dia como uma linha horizontal. A plotagem pode ser limitada até um certo horário (16:30 por padrão).

- **[AUTOFIBO](estratégias/exemplos/editaveis/indicadores/price_action/AUTOFIBO.txt)**
  Plota retrações de Fibonacci automaticamente com base em topos e fundos detectados.

- **[Body_Gaps](estratégias/exemplos/editaveis/indicadores/price_action/Body_Gaps.txt)**
  Detecta e colore gaps formados entre os corpos (abertura/fechamento) de candles consecutivos.

- **[acima](estratégias/exemplos/editaveis/indicadores/price_action/acima.txt)**
  Regra de coloração simples que pinta o candle de verde se o preço estiver acima da abertura do dia.

- **[candlestick](estratégias/exemplos/editaveis/indicadores/price_action/candlestick.txt)**
  Regra de coloração complexa que identifica e colore diversos padrões de candlestick (Doji, Martelo, Estrela Cadente, Engolfo, Harami).

- **[CandlestickType](estratégias/exemplos/editaveis/indicadores/price_action/CandlestickType.txt)**
  Identifica e colore tipos específicos de candlestick (Martelo, Martelo Invertido, Doji) em gráficos Heikin Ashi.

- **[DOIS2junto](estratégias/exemplos/editaveis/indicadores/price_action/DOIS2junto.txt)**
  Plota dois conjuntos de níveis percentuais de Fibonacci.

- **[Donchian_Fibonacci](estratégias/exemplos/editaveis/indicadores/price_action/Donchian_Fibonacci.txt)**
  Plota níveis de Fibonacci dentro de um Canal de Donchian, com opções para plotar diferentes níveis.

- **[Donchian_Fibonacci_2](estratégias/exemplos/editaveis/indicadores/price_action/Donchian_Fibonacci_2.txt)**
  Plota níveis de Fibonacci dentro de um Canal de Donchian.

- **[FalsoRompimento](estratégias/exemplos/editaveis/indicadores/price_action/FalsoRompimento.txt)**
  Detecta falsos rompimentos de máximas/mínimas e gera alertas.

- **[Fibo_Bands](estratégias/exemplos/editaveis/indicadores/price_action/Fibo_Bands.txt)**
  Plota bandas de Fibonacci baseadas em um preço central e Average True Range.

- **[Fibo_Bands0](estratégias/exemplos/editaveis/indicadores/price_action/Fibo_Bands0.txt)**
  Outra versão das bandas de Fibonacci.

- **[Fibo_Bands1](estratégias/exemplos/editaveis/indicadores/price_action/Fibo_Bands1.txt)**
  Plota bandas de Fibonacci baseadas em um preço central e no Average True Range, com níveis de extensão.

- **[Fibo_Bands2](estratégias/exemplos/editaveis/indicadores/price_action/Fibo_Bands2.txt)**
  Plota bandas de Fibonacci baseadas em um preço central e no Average True Range, com níveis de retração.

- **[Fibo_Bands3](estratégias/exemplos/editaveis/indicadores/price_action/Fibo_Bands3.txt)**
  Plota bandas de Fibonacci baseadas em um preço central e no Average True Range, com níveis de extensão negativos.

- **[Stormer](estrategias/exemplos/editaveis/indicadores/price_action/Stormer)**
  Regra de coloração que identifica padrões de candles de reversão (fechamento maior/menor que o anterior e mínimas/máximas relativas).

- **[V0034_Williams_Find_Market_Bottoms](estrategias/exemplos/editaveis/indicadores/price_action/V0034_Williams_Find_Market_Bottoms.txt)**
  Indicador que busca por fundos de mercado utilizando o Williams %R e Bandas de Bollinger.

- **[V0035_Wilson_Relative_Price_Channel](estrategias/exemplos/editaveis/indicadores/price_action/V0035_Wilson_Relative_Price_Channel.txt)**
  Indicador que plota um canal de preço relativo baseado no RSI.

- **[V0039_Tweezers](estrategias/exemplos/editaveis/indicadores/price_action/V0039_Tweezers.txt)**
  Regra de coloração que identifica padrões de "Tweezers" (pinças) de alta ou baixa.

- **[V0047_TOPOS_FUNDOS(COD1)](estrategias/exemplos/editaveis/indicadores/price_action/V0047_TOPOS_FUNDOS(COD1).txt)**
  Indicador que tenta detectar e plotar topos e fundos, mas com ressalvas de funcionamento.

- **[V0048_Top_e_Fun_Color](estrategias/exemplos/editaveis/indicadores/price_action/V0048_Top_e_Fun_Color.txt)**
  Regra de coloração que pinta os candles de forma diferente dependendo da sequência de topos e fundos detectados.

### Tendência
- **[___TRIPLE_MEDIAEXP](estratégias/exemplos/editaveis/indicadores/tendencia/___TRIPLE_MEDIAEXP.txt)**
  Plota três médias móveis exponenciais com períodos múltiplos (ex: 9, 18, 36), servindo como um 'leque' de médias para identificar tendência.

- **[___TSTE_ADX](estratégias/exemplos/editaveis/indicadores/tendencia/___TSTE_ADX.txt)**
  Plota o indicador ADX e as linhas DI+/DI-, colorindo as barras para indicar força e direção da tendência.

- **[__AUTO_LTA_LTB](estratégias/exemplos/editaveis/indicadores/tendencia/__AUTO_LTA_LTB.txt)**
  Indicador que tenta desenhar Linhas de Tendência de Alta (LTA) e Baixa (LTB) de forma automática, ajustando-se dinamicamente ao preço.

- **[__ElderImpulse](estratégias/exemplos/editaveis/indicadores/tendencia/__ElderImpulse.txt)**
  Implementa o 'Elder Impulse System', que colore as barras com base na inclinação de uma MME e na direção do histograma MACD, para identificar momentos de concordância de tendência.

- **[__INDICADOR_TESTE_TOPOS](estratégias/exemplos/editaveis/indicadores/tendencia/__INDICADOR_TESTE_TOPOS.txt)**
  Indicador que usa uma VMA (Média Móvel Variável) e colore as barras de acordo com a tendência, também plotando topos e fundos.

- **[__MEDIAMOVELTRIPLA](estratégias/exemplos/editaveis/indicadores/tendencia/__MEDIAMOVELTRIPLA.txt)**
  Implementação do TEMA (Triple Exponential Moving Average), uma média móvel com menos lag que a MME tradicional.

- **[__SUPER_TREND](estratégias/exemplos/editaveis/indicadores/tendencia/__SUPER_TREND.txt)**
  Indicador seguidor de tendência que colore as barras de acordo com a direção do movimento, similar ao HiLo Activator mas com lógica de contagem de barras.

- **[__VECTOR_FLOW_COR](estratégias/exemplos/editaveis/indicadores/tendencia/__VECTOR_FLOW_COR.txt)**
  Regra de coloração que utiliza o indicador `VectorFlowChannel` para pintar os candles de verde (alta) ou vermelho (baixa).

- **[_AGULHADA](estratégias/exemplos/editaveis/indicadores/tendencia/_AGULHADA.txt)**
  Busca por um padrão de 'agulhada' nos indicadores DI+/DI-, colorindo o candle quando o ADX confirma a tendência.

- **[_COLORACAO_CRUZAMENTO_MEDIAS](estratégias/exemplos/editaveis/indicadores/tendencia/_COLORACAO_CRUZAMENTO_MEDIAS.txt)**
  Regra de coloração que pinta os candles baseado no cruzamento de duas médias móveis ponderadas (`WAverage`).

- **[_COR_CRUZAMENTOS_MACD_DIDI](estratégias/exemplos/editaveis/indicadores/tendencia/_COR_CRUZAMENTOS_MACD_DIDI.txt)**
  Regra de coloração que exige uma confluência de três indicadores de tendência (Médias, DI+/DI- e MACD) para pintar o candle.

- **[_COR_DI_ADX](estratégias/exemplos/editaveis/indicadores/tendencia/_COR_DI_ADX.txt)**
  Pinta os candles de acordo com a força (ADX) e direção (DI+/DI-) da tendência.

- **[_CRUZAMENTO_MEDIA51](estratégias/exemplos/editaveis/indicadores/tendencia/_CRUZAMENTO_MEDIA51.txt)**
  Regra de coloração simples que pinta os candles de verde/vermelho se o preço está acima/abaixo de uma média de 51 períodos.

- **[_Cruzamento_WMA](estratégias/exemplos/editaveis/indicadores/tendencia/_Cruzamento_WMA.txt)**
  Pinta os candles de azul/vermelho no momento exato do cruzamento de duas médias móveis ponderadas (`WAverage`).

- **[_DELOREAN](estratégias/exemplos/editaveis/indicadores/tendencia/_DELOREAN.txt)**
  Plota médias móveis deslocadas para frente (usando `MaxBarsForward`), uma tentativa de 'prever' a direção futura do preço.

- **[_Estudo de tendência](estratégias/exemplos/editaveis/indicadores/tendencia/_Estudo de tendência.txt)**
  Plota duas médias exponenciais e colore os candles de acordo com a posição do preço em relação a elas.

- **[_LINHA_CRUZAMENTO_MEDIASPONDERADA](estratégias/exemplos/editaveis/indicadores/tendencia/_LINHA_CRUZAMENTO_MEDIASPONDERADA.txt)**
  Plota linhas de tendência e colore candles baseado no cruzamento de médias ponderadas.

- **[_LINHAS_CRUZAMENTO_MEDIAS](estratégias/exemplos/editaveis/indicadores/tendencia/_LINHAS_CRUZAMENTO_MEDIAS.txt)**
  Similar ao anterior, mas usa médias exponenciais.

- **[_RT_](estratégias/exemplos/editaveis/indicadores/tendencia/_RT_.txt)**
  Regra de coloração que combina sinais de médias móveis e do oscilador estocástico para pintar os candles.

- **[_TESTE_COR_INPUT](estratégias/exemplos/editaveis/indicadores/tendencia/_TESTE_COR_INPUT.txt)**
  Script de teste que colore as barras baseado em um cruzamento de médias, permitindo que o usuário defina as cores via `input`.

- **[ALMAv](estratégias/exemplos/editaveis/indicadores/tendencia/ALMAv.txt)**
  Implementação da Média Móvel de Arnaud Legoux (ALMA), conhecida por ser responsiva e suave.

- **[AUTO_LTA_LTB](estratégias/exemplos/editaveis/indicadores/tendencia/AUTO_LTA_LTB.txt)**
  Outra implementação de um indicador que tenta desenhar linhas de tendência de alta e baixa automaticamente.

- **[Accumulative_Swing_Index(ASI)](estratégias/exemplos/editaveis/indicadores/tendencia/Accumulative_Swing_Index(ASI).txt)**
  Implementação do Índice de Oscilação Acumulada (ASI) de Welles Wilder, um oscilador de momento.

- **[Average_Penetration_Indicator](estratégias/exemplos/editaveis/indicadores/tendencia/Average_Penetration_Indicator.txt)**
  Indicador customizado que mede o quanto o preço 'penetra' uma média móvel.

- **[Bears_Bulls](estratégias/exemplos/editaveis/indicadores/tendencia/Bears_Bulls.txt)**
  Implementação dos indicadores Bulls Power e Bears Power de Alexander Elder.

- **[BULLPOWERCOLOR](estratégias/exemplos/editaveis/indicadores/tendencia/BULLPOWERCOLOR.txt)**
  Regra de coloração que combina Bull Power com uma média móvel para confirmar tendência de alta.

- **[Bull_Bears_Control](estratégias/exemplos/editaveis/indicadores/tendencia/Bull_Bears_Control.txt)**
  Indicador que conta o número de barras consecutivas fechando acima ou abaixo do ponto médio da barra anterior.

- **[COLOR_IFDT](estratégias/exemplos/editaveis/indicadores/tendencia/COLOR_IFDT.txt)**
  Colore as barras com base no valor do indicador IFDT.

- **[Coloracao_ADX](estratégias/exemplos/editaveis/indicadores/tendencia/Coloracao_ADX.txt)**
  Colore as barras de vermelho se o ADX estiver dentro de uma faixa específica (31-35).

- **[cruzamento_de_medias_ponderadas](estratégias/exemplos/editaveis/indicadores/tendencia/cruzamento_de_medias_ponderadas.txt)**
  Colore as barras com base no cruzamento de médias móveis ponderadas da abertura e do fechamento.

- **[Cruzamento_Medias](estratégias/exemplos/editaveis/indicadores/tendencia/Cruzamento_Medias.txt)**
  Colore as barras com base no cruzamento de duas médias móveis exponenciais.

- **[cTrendflex](estratégias/exemplos/editaveis/indicadores/tendencia/cTrendflex.txt)**
  Implementação do 'Trendflex Indicator' de John Ehlers, que mede a força e direção da tendência.

- **[DIDIINDEX_comADX](estratégias/exemplos/editaveis/indicadores/tendencia/DIDIINDEX_comADX.txt)**
  Colore as barras com base no cruzamento das linhas do Didi Index, filtrado por condições do ADX e DI+/DI-.

- **[Difusor_Fluxo_LongShort_Santo](estratégias/exemplos/editaveis/indicadores/tendencia/Difusor_Fluxo_LongShort_Santo.txt)**
  Indicador 'Santo' complexo que utiliza MACD, médias móveis e níveis de Fibonacci para colorir barras e plotar linhas.

- **[Difusor_Fluxo_LongShort_santo2](estratégias/exemplos/editaveis/indicadores/tendencia/Difusor_Fluxo_LongShort_santo2.txt)**
  Outra versão do indicador 'Santo', com parâmetros e condições ligeiramente diferentes.

- **[DImaisDImenosADX](estratégias/exemplos/editaveis/indicadores/tendencia/DImaisDImenosADX.txt)**
  Plota DI+, DI- e ADX, colorindo as barras com base na sua relação.

- **[Double_Exponential_Moving_Average(DEMA)](estratégias/exemplos/editaveis/indicadores/tendencia/Double_Exponential_Moving_Average(DEMA).txt)**
  Plota uma Média Móvel Exponencial Dupla (DEMA) e colore as barras com base na posição do preço em relação a ela.

- **[Half_Trend](estratégias/exemplos/editaveis/indicadores/tendencia/Half_Trend.txt)**
  Indicador seguidor de tendência que colore as barras de acordo com a direção do movimento.

- **[Inflex_ADX_certo](estratégias/exemplos/editaveis/indicadores/tendencia/Inflex_ADX_certo.src)**
  Regra de coloração que pinta os candles com base na inflexão do ADX.

- **[Inflex_ADX](estratégias/exemplos/editaveis/indicadores/tendencia/Inflex_ADX.src)**
  Regra de coloração que pinta os candles com base na inflexão do ADX.

- **[LACRAIA](estratégias/exemplos/editaveis/indicadores/tendencia/LACRAIA.txt)**
  Regra de coloração que combina médias móveis para indicar a tendência.

- **[Linear_Regression](estratégias/exemplos/editaveis/indicadores/tendencia/Linear_Regression.src)**
  Plota uma linha de regressão linear.

- **[Linha de inflexão](estratégias/exemplos/editaveis/indicadores/tendencia/Linha de inflexão.txt)**
  Indicador e regra de coloração para auxiliar em tomada de decisão.

- **[Linhas_de_Regressao](estratégias/exemplos/editaveis/indicadores/tendencia/Linhas_de_Regressao.src)**
  Plota múltiplos canais de regressão linear.

- **[LTA_LTB_Kastor](estratégias/exemplos/editaveis/indicadores/tendencia/LTA_LTB_Kastor.txt)**
  Indicador que tenta desenhar Linhas de Tendência de Alta (LTA) e Baixa (LTB).

- **[LWMAv](estratégias/exemplos/editaveis/indicadores/tendencia/LWMAv.txt)**
  Implementação da Média Móvel Ponderada Linearmente (LWMA).

- **[MA_Trend_Colored](estratégias/exemplos/editaveis/indicadores/tendencia/MA_Trend_Colored.txt)**
  Indicador de tendência que colore as barras com base na relação entre duas médias móveis.

- **[MEDIA_COM_DATA](estratégias/exemplos/editaveis/indicadores/tendencia/MEDIA_COM_DATA.txt)**
  Plota uma média móvel de fechamentos diários com base em um período de dias.

- **[mediadiaria](estratégias/exemplos/editaveis/indicadores/tendencia/mediadiaria.txt)**
  Plota a média dos fechamentos dos últimos 9 dias.

- **[MEDIALEKKE](estratégias/exemplos/editaveis/indicadores/tendencia/MEDIALEKKE.txt)**
  Plota um "leque" de médias exponenciais que funcionam como suportes.

- **[MIMA](estratégias/exemplos/editaveis/indicadores/tendencia/MIMA.txt)**
  Indicador que plota uma média móvel exponencial de um valor calculado a partir de níveis de Fibonacci e máximas/mínimas.

- **[NIVEIS_DO_RSI](estratégias/exemplos/editaveis/indicadores/tendencia/NIVEIS_DO_RSI.txt)**
  Plota os níveis de máxima e mínima do RSI.

- **[novepontodois](estratégias/exemplos/editaveis/indicadores/tendencia/novepontodois.txt)**
  Colore as barras com base na relação do fechamento com o fechamento anterior e uma média exponencial de 9 períodos.

- **[OZZYMANDIAS](estratégias/exemplos/editaveis/indicadores/tendencia/OZZYMANDIAS.txt)**
  Colore as barras e plota uma linha de tendência baseada em médias e ATR.

- **[PhiCube_SANTO_Bandas](estratégias/exemplos/editaveis/indicadores/tendencia/PhiCube_SANTO_Bandas.src)**
  Plota e colore as barras com base em um indicador "Santo" (SMMA) e bandas de preço, com filtros de médias e sinais de alerta.

- **[PhiCube_SANTO](estratégias/exemplos/editaveis/indicadores/tendencia/PhiCube_SANTO.src)**
  Plota e colore as barras com base em um indicador "Santo" (SMMA) e níveis PhiCube.

- **[Phicube_SANTO](estratégias/exemplos/editaveis/indicadores/tendencia/Phicube_SANTO.txt)**
  Plota e colore as barras com base em um indicador "Santo" (SMMA) e níveis PhiCube.

- **[Rainbow4](estratégias/exemplos/editaveis/indicadores/tendencia/Rainbow4.src)**
  Plota um conjunto de médias móveis exponenciais (65, 70, 75, 80).

- **[Rainbow5](estratégias/exemplos/editaveis/indicadores/tendencia/Rainbow5.src)**
  Plota um conjunto de médias móveis exponenciais (85, 90, 95, 100).

- **[Relacao_Preco_Medias](estratégias/exemplos/editaveis/indicadores/tendencia/Relacao_Preco_Medias.src)**
  Plota a contagem de vezes que o preço de fechamento está acima ou abaixo de uma série de médias móveis de diferentes períodos.

- **[SMMA](estrategias/exemplos/editaveis/indicadores/tendencia/SMMA.src)**
  Implementação da média móvel suavizada (SMMA), que oferece uma suavização mais lenta que a média exponencial.

- **[SMMAv](estrategias/exemplos/editaveis/indicadores/tendencia/SMMAv.src)**
  Variação da média móvel suavizada (SMMA) com cálculo de inclinação, útil para identificar a direção da tendência.
- **[STP0010_Trade_e_Acoes_Indicador_Media_9_Mais_200](estrategias/exemplos/editaveis/indicadores/tendencia/STP0010_Trade_e_Acoes_Indicador_Media_9_Mais_200.txt)**
  Indicador que plota duas linhas de preço baseadas em uma Média Móvel Exponencial de 9 períodos, deslocadas em +200 e -200 unidades.
- **[Super_Trend](estrategias/exemplos/editaveis/indicadores/tendencia/Super_Trend)**
  Indicador seguidor de tendência que colore as barras de acordo com a direção do movimento, similar ao HiLo Activator mas com lógica de contagem de barras.
- **[tabajara_candlestick](estrategias/exemplos/editaveis/indicadores/tendencia/tabajara_candlestick.src)**
  Regra de coloração que pinta os candles de acordo com a direção do preço em relação a uma média móvel de 20 períodos.
- **[V0002_VENO_ANGLE(LTA_LTB)](estrategias/exemplos/editaveis/indicadores/tendencia/V0002_VENO_ANGLE(LTA_LTB).txt)**
  Indicador que plota linhas de tendência de alta (LTA) e baixa (LTB) com ângulos predefinidos.
- **[V0004_Veno_exp_triple](estrategias/exemplos/editaveis/indicadores/tendencia/V0004_Veno_exp_triple.txt)**
  Indicador que plota médias móveis exponenciais triplas.
- **[V0006_ATEMP_VNZ_MM](estrategias/exemplos/editaveis/indicadores/tendencia/V0006_ATEMP_VNZ_MM.txt)**
  Indicador que plota a média de 9 períodos do diário em tempos gráficos menores.
- **[V0007_VMA'z](estrategias/exemplos/editaveis/indicadores/tendencia/V0007_VMA'z.txt)**
  Indicador que plota a variação da média móvel (VMA), colorindo a linha de acordo com a direção do preço.
- **[V0008_VectorFlowChannel](estrategias/exemplos/editaveis/indicadores/tendencia/V0008_VectorFlowChannel.txt)**
  Indicador que plota linhas de tendência suavizadas baseadas em topos e fundos.
- **[V0011_VMA_Simple](estrategias/exemplos/editaveis/indicadores/tendencia/V0011_VMA_Simple.txt)**
  Indicador que plota uma média móvel suavizada (VMA) e colore os candles de acordo com a posição do preço em relação a ela.
- **[V0033_Moving_WellesWilder](estrategias/exemplos/editaveis/indicadores/tendencia/V0033_Moving_WellesWilder.txt)**
  Implementação da Média Móvel Aritmética de Welles Wilder.
- **[V0041_TripleMovingHeikin](estrategias/exemplos/editaveis/indicadores/tendencia/V0041_TripleMovingHeikin.txt)**
  Indicador que plota três médias móveis baseadas em Heikin Ashi e preço típico, colorindo os candles de acordo com a tendência.
- **[V0043_UnoTEMA](estrategias/exemplos/editaveis/indicadores/tendencia/V0043_UnoTEMA.txt)**
  Indicador que plota a Triple Exponential Moving Average (TEMA) e colore os candles de acordo com a posição do preço em relação a ela.
- **[V0044_Traders_Dynamic_Index(TDI)](estrategias/exemplos/editaveis/indicadores/tendencia/V0044_Traders_Dynamic_Index(TDI).txt)**
  Indicador que combina RSI, Bandas de Bollinger e médias móveis para identificar a direção e força da tendência.
- **[V0054_MIMA](estrategias/exemplos/editaveis/indicadores/tendencia/V0054_MIMA.txt)**
  Indicador que plota uma média móvel exponencial de um valor calculado a partir de níveis de Fibonacci e máximas/mínimas.
- **[V0057_TEMA_Color](estrategias/exemplos/editaveis/indicadores/tendencia/V0057_TEMA_Color.txt)**
  Regra de coloração que pinta os candles de acordo com a posição do preço em relação à Triple Exponential Moving Average (TEMA).
- **[V0059_MEDIA66_COLOR](estrategias/exemplos/editaveis/indicadores/tendencia/V0059_MEDIA66_COLOR.txt)**
  Regra de coloração que pinta os candles de acordo com a posição do preço em relação a uma média móvel exponencial de 66 períodos.

### Volatilidade
- **[5%_mme9](estratégias/exemplos/editaveis/indicadores/volatilidade/5%_mme9.txt)**
  Indicador que gera um alerta visual quando o preço de fechamento se desvia 5% para cima ou para baixo de uma Média Móvel Exponencial de 9 períodos.
  * **Alerta de Alta:** `alert(clgreen)` se `close >= mme * 1.05`.
  * **Alerta de Baixa:** `alert(clred)` se `close <= mme * 0.95`.

- **[A011_QS_BB](estratégias/exemplos/editaveis/indicadores/volatilidade/A011_QS_BB.txt)**
  Indicador extremamente complexo que plota Bandas de Bollinger avançadas no gráfico. Utiliza uma vasta gama de outros indicadores (MAMA, FAMA, Holt EMA, ALMA, MACD, Damiani Volatmeter) como filtros e condições para a coloração das bandas e para gerar alertas. A lógica é muito densa e multifacetada, focada em fornecer um sinal de volatilidade e tendência altamente filtrado.

- **[__BANDAS_DE_HILOW](estratégias/exemplos/editaveis/indicadores/volatilidade/__BANDAS_DE_HILOW.txt)**
  Cria um canal de volatilidade similar a Bandas de Keltner, usando a média do `TrueRange` para definir a largura das bandas em volta de uma média central.

- **[_ACBRITO_FREQ_MERCADO_WDO](estratégias/exemplos/editaveis/indicadores/volatilidade/_ACBRITO_FREQ_MERCADO_WDO.txt)**
  Regra de coloração que mede a 'frequência' do mercado (range do candle) para o mini-dólar (WDO), colorindo as barras para indicar volatilidade baixa, normal ou alta.

- **[_ACBRITO_FREQ_MERCADO_WIN](estratégias/exemplos/editaveis/indicadores/volatilidade/_ACBRITO_FREQ_MERCADO_WIN.txt)**
  Similar ao anterior, mas com parâmetros ajustados para o mini-índice (WIN).

- **[_CANAL_MAXIMO_MINIMO](estratégias/exemplos/editaveis/indicadores/volatilidade/_CANAL_MAXIMO_MINIMO.txt)**
  Desenha um canal com base nas máximas e mínimas de um período definido, útil para visualizar a volatilidade e zonas de suporte/resistência.

- **[ATR](estratégias/exemplos/editaveis/indicadores/volatilidade/ATR.txt)**
  Implementação padrão do indicador Average True Range (ATR) de Welles Wilder.

- **[BBollinger_Scalper](estratégias/exemplos/editaveis/indicadores/volatilidade/BBollinger_Scalper.txt)**
  Indicador complexo para scalping que combina Bandas de Bollinger, Canais de Keltner e Filtros de Kalman para gerar sinais visuais.

- **[BuyAndSell_Sign](estratégias/exemplos/editaveis/indicadores/volatilidade/BuyAndSell_Sign.txt)**
  Plota uma 'Linha de Tendência' baseada em Bandas de Bollinger e ATR, colorindo as barras e gerando alertas.

- **[Chandelier_Stop(Exit)](estratégias/exemplos/editaveis/indicadores/volatilidade/Chandelier_Stop(Exit).txt)**
  Plota a linha do Chandelier Stop e colore as barras de acordo com a posição do preço em relação a ela.

- **[DesviKCfundo](estratégias/exemplos/editaveis/indicadores/volatilidade/DesviKCfundo.txt)**
  Plota as bandas superior e inferior do Canal de Keltner.

- **[Envelope_Perc](estratégias/exemplos/editaveis/indicadores/volatilidade/Envelope_Perc.txt)**
  Plota um envelope dinâmico em torno de uma média móvel, onde a largura percentual se ajusta para conter uma certa porcentagem de preços passados.

- **[V0062_StopATRColor](estrategias/exemplos/editaveis/indicadores/volatilidade/V0062_StopATRColor.txt)**
  Regra de coloração que pinta os candles de verde se o fechamento estiver acima do Stop ATR e de vermelho se estiver abaixo.

### Volume
- **[___Vol001](estratégias/exemplos/editaveis/indicadores/volume/___Vol001.txt)**
  Plota o volume acumulado (`Summation`) ao longo de um período, útil para identificar picos de volume.

- **[__AGRESSAO_DE_COMPRAEVENDA](estratégias/exemplos/editaveis/indicadores/volume/__AGRESSAO_DE_COMPRAEVENDA.txt)**
  Oscilador de agressão que acumula o saldo de agressão (`AgressionVolBalance`) ou o volume de compra/venda, reiniciando o acúmulo quando uma Média Móvel de Hull vira.

- **[__AGRESSAO_HISTOGRAMA](estratégias/exemplos/editaveis/indicadores/volume/__AGRESSAO_HISTOGRAMA.txt)**
  Versão para histograma do indicador `__AGRESSAO_DE_COMPRAEVENDA`.

- **[__MAIOR_VOLUME](estratégias/exemplos/editaveis/indicadores/volume/__MAIOR_VOLUME.txt)**
  Identifica o candle de maior volume dentro de um período e plota uma linha horizontal no seu preço de fechamento.

- **[__NIVEL_DEVOLUME_FINANCEIRO](estratégias/exemplos/editaveis/indicadores/volume/__NIVEL_DEVOLUME_FINANCEIRO.txt)**
  Plota o range (máxima e mínima) do candle que teve o maior volume financeiro dentro de um período, criando uma 'zona de volume'.

- **[__VIPER_LINES](estratégias/exemplos/editaveis/indicadores/volume/__VIPER_LINES.txt)**
  Plota o saldo de agressão como um histograma e colore as barras de acordo com a predominância de compradores ou vendedores.

- **[__VOLUME_ACUMULACAO](estratégias/exemplos/editaveis/indicadores/volume/__VOLUME_ACUMULACAO.txt)**
  Implementação do indicador 'Weis Wave Volume', que acumula o volume em 'ondas' de alta e de baixa, mostrando a força por trás de cada movimento.

- **[__VWAP_COM_PORCENTO](estratégias/exemplos/editaveis/indicadores/volume/__VWAP_COM_PORCENTO.txt)**
  Plota a VWAP de um dia anterior e bandas percentuais acima e abaixo dela.

- **[__VWAP_DIAS_ATRAS](estratégias/exemplos/editaveis/indicadores/volume/__VWAP_DIAS_ATRAS.txt)**
  Plota a linha de VWAP de um dia anterior especificado no gráfico atual.

- **[__VWAP_DIAS_ATRAS2](estratégias/exemplos/editaveis/indicadores/volume/__VWAP_DIAS_ATRAS2.txt)**
  Outra implementação para plotar a VWAP do dia anterior.

- **[__WaveWeisHMA](estratégias/exemplos/editaveis/indicadores/volume/__WaveWeisHMA.txt)**
  Uma variação do 'Weis Wave Volume' que usa uma Média Móvel de Hull (HMA) para definir as 'ondas' de preço, acumulando o volume em cada uma.

- **[__WVAP_MAX](estratégias/exemplos/editaveis/indicadores/volume/__WVAP_MAX.txt)**
  Calcula e plota a VWAP ponderada pela máxima (`High`) do dia, com bandas de suporte/resistência baseadas no `TrueRange`.

- **[_ColacinoAgressao](estratégias/exemplos/editaveis/indicadores/volume/_ColacinoAgressao.txt)**
  Indicador de agressão que utiliza filtros (High-pass e SuperSmoother de John Ehlers) para suavizar o saldo de agressão e identificar a direção da força do mercado.

- **[_SatosComLinha](estratégias/exemplos/editaveis/indicadores/volume/_SatosComLinha.txt)**
  Colore as barras com base no volume em relação a uma média de volume e plota linhas nos níveis de abertura/fechamento das barras de alto volume.

- **[_SmartBar](estratégias/exemplos/editaveis/indicadores/volume/_SmartBar.txt)**
  Regra de coloração que colore as barras com base em múltiplos do desvio padrão do volume, identificando barras com volume normal, alto ou extremo.

- **[_VEISS_VOLUME](estratégias/exemplos/editaveis/indicadores/volume/_VEISS_VOLUME.txt)**
  Implementação do oscilador de volume de Weis, que relaciona o volume com o range do candle.

- **[_VENO_LINES_WAP](estratégias/exemplos/editaveis/indicadores/volume/_VENO_LINES_WAP.txt)**
  Plota níveis de Fibonacci baseados na VWAP do dia anterior.

- **[_VENOM_SMART_BAR](estratégias/exemplos/editaveis/indicadores/volume/_VENOM_SMART_BAR.txt)**
  Regra de coloração complexa que analisa o fluxo de agressão e volume para identificar barras 'smart'.

- **[_VOLUME_MAIOR_MENOR](estratégias/exemplos/editaveis/indicadores/volume/_VOLUME_MAIOR_MENOR.txt)**
  Plota o volume de compra e venda em um histograma, destacando a força predominante.

- **[_VWAP_DELTA_DIARIO](estratégias/exemplos/editaveis/indicadores/volume/_VWAP_DELTA_DIARIO.txt)**
  Calcula e plota a VWAP do saldo de agressão diário.

- **[_VWAP_DIAS_ANTERIORES](estratégias/exemplos/editaveis/indicadores/volume/_VWAP_DIAS_ANTERIORES.txt)**
  Plota a VWAP de um dia anterior específico.

- **[_VWAP_LINES_v2](estratégias/exemplos/editaveis/indicadores/volume/_VWAP_LINES_v2.txt)**
  Plota as VWAPs diária, semanal e mensal.

- **[_hist_Agress_ll](estratégias/exemplos/editaveis/indicadores/volume/_hist_Agress_ll.txt)**
  Indicador de agressão no estilo Weis Wave, que acumula o saldo de agressão em ondas de alta e baixa.

- **[_JS_Santo_VAS](estratégias/exemplos/editaveis/indicadores/volume/_JS_Santo_VAS.txt)**
  Oscilador complexo que combina saldo de agressão, volume e o spread do candle para criar um indicador de fluxo de sentimento.

- **[_JS_Volume_VAS](estratégias/exemplos/editaveis/indicadores/volume/_JS_Volume_VAS.txt)**
  Calcula a 'força' de cada candle multiplicando o spread pelo volume e saldo de agressão.

- **[_MEDIA_VOLUME_FIBONACCI](estratégias/exemplos/editaveis/indicadores/volume/_MEDIA_VOLUME_FIBONACCI.txt)**
  Plota uma média móvel do preço apenas nos candles cujo volume ultrapassa um múltiplo (fator de Fibonacci) da média de volume.

- **[_TESTE_VWAP](estratégias/exemplos/editaveis/indicadores/volume/_TESTE_VWAP.txt)**
  Script de teste para plotar a VWAP de um dia específico no passado.

- **[_TESTE_WVAP_DIAS](estratégias/exemplos/editaveis/indicadores/volume/_TESTE_WVAP_DIAS.txt)**
  Plota a VWAP dos últimos 4 dias no gráfico.

- **[AGRESSAO](estratégias/exemplos/editaveis/indicadores/volume/AGRESSAO.txt)**
  Regra de coloração baseada no `volume_Accumulation_Percentage_Indicator`.

- **[AccVolWave](estratégias/exemplos/editaveis/indicadores/volume/AccVolWave.txt)**
  Indicador no estilo Weis Wave que acumula volume e saldo de agressão baseado na direção de uma Média Móvel de Hull.

- **[Acumulacao_Distribuicao_Classical_MT](estratégias/exemplos/editaveis/indicadores/volume/Acumulacao_Distribuicao_Classical_MT.txt)**
  Indicador clássico de Acumulação/Distribuição.

- **[Acumulado_Dia](estratégias/exemplos/editaveis/indicadores/volume/Acumulado_Dia.txt)**
  Plota o somatório do volume de agressão de compra e venda desde a abertura do dia.

- **[Agressão_Oscilador](estratégias/exemplos/editaveis/indicadores/volume/Agressão_Oscilador.txt)**
  Plota o volume de agressão de compra e de venda como duas linhas de um oscilador.

- **[Agression_Letti](estratégias/exemplos/editaveis/indicadores/volume/Agression_Letti.txt)**
  Indicador que aplica uma regressão linear sobre o saldo de agressão para tentar antecipar movimentos.

- **[AgressiveBars](estratégias/exemplos/editaveis/indicadores/volume/AgressiveBars.txt)**
  Colore as barras com base no desvio padrão do saldo de agressão em relação à sua média.

- **[Alarme_Absorcao](estratégias/exemplos/editaveis/indicadores/volume/Alarme_Absorcao.txt)**
  Gera um alarme ao detectar um padrão de absorção (alto volume com baixo range).

- **[BalanceOfPowerTrend](estratégias/exemplos/editaveis/indicadores/volume/BalanceOfPowerTrend.txt)**
  Versão suavizada do indicador 'Balance of Power', que mede a força de compradores versus vendedores.

- **[Better_Volume_Adapted](estratégias/exemplos/editaveis/indicadores/volume/Better_Volume_Adapted.txt)**
  Adaptação do indicador 'Better Volume', que colore as barras de acordo com o volume e o range.

- **[color_bull](estratégias/exemplos/editaveis/indicadores/volume/color_bull.txt)**
  Colore as barras de verde se o número de trades for maior que o `bullPower`.

- **[corWEISS](estratégias/exemplos/editaveis/indicadores/volume/corWEISS.txt)**
  Colore as barras com base no indicador `wwEISSWAVE2`.

- **[MEDIDOR_DE_AGRESSAO](estratégias/exemplos/editaveis/indicadores/volume/MEDIDOR_DE_AGRESSAO.txt)**
  Plota o volume de agressão de compra e venda.

- **[PINTA_VOLUME](estratégias/exemplos/editaveis/indicadores/volume/PINTA_VOLUME.src)**
  Colore as barras com base na relação entre o volume financeiro e o range do candle, classificando-as em categorias como "Correspondência", "Anomalia" e "Armadilha".

- **[V0010_VENO_WAP](estrategias/exemplos/editaveis/indicadores/volume/V0010_VENO_WAP.txt)**
  Regra de coloração que colore os candles de verde se estiverem acima da VWAP e de vermelho se estiverem abaixo.

- **[V0013_Vol_Acum_Perc_Ind](estrategias/exemplos/editaveis/indicadores/volume/V0013_Vol_Acum_Perc_Ind.txt)**
  Indicador que plota a porcentagem acumulada do volume.
- **[V0014_Vol_Color_Bars](estrategias/exemplos/editaveis/indicadores/volume/V0014_Vol_Color_Bars.txt)**
  Regra de coloração que colore as barras de acordo com o volume (alto, normal, baixo).
- **[V0015_High_Volum_bar](estrategias/exemplos/editaveis/indicadores/volume/V0015_High_Volum_bar.txt)**
  Regra de coloração que colore as barras conf volume e nivel de fibo parametrizavel.

- **[V0016_Med_Cumulative_Range_Vortex](estrategias/exemplos/editaveis/indicadores/volume/V0016_Med_Cumulative_Range_Vortex.txt)**
  Regra de coloração que colore as barras com base na acumulação dos resultados das máximas e mínimas divididas pelo true range.
- **[V0018_MAx_VWap_Intraday](estrategias/exemplos/editaveis/indicadores/volume/V0018_MAx_VWap_Intraday.txt)**
  Indicador que plota a VWAP intraday da máxima do dia.

- **[V0019_VWAP_IT_MAX_FIBO](estrategias/exemplos/editaveis/indicadores/volume/V0019_VWAP_IT_MAX_FIBO.txt)**
  Indicador que plota a VWAP intraday da máxima com níveis de Fibonacci.
- **[V0020_VWAP_IT_MIN](estrategias/exemplos/editaveis/indicadores/volume/V0020_VWAP_IT_MIN.txt)**
  Indicador que plota a VWAP intraday da mínima.
- **[V0021_VWAP_IT_MIN_FIBO](estrategias/exemplos/editaveis/indicadores/volume/V0021_VWAP_IT_MIN_FIBO.txt)**
  Indicador que plota a VWAP intraday da mínima com níveis de Fibonacci.

- **[V0022_CHANEL_VWAP_Range](estrategias/exemplos/editaveis/indicadores/volume/V0022_CHANEL_VWAP_Range.txt)**
  Indicador que plota a VWAP intraday semanal e mensal como um range.
- **[V0023_VWAP_DELTA](estrategias/exemplos/editaveis/indicadores/volume/V0023_VWAP_DELTA.txt)**
  Indicador que plota um histograma de agressão sobre a VWAP calculada e ponderada pelo delta.
- **[V0024_VWAP_of_Obv](estrategias/exemplos/editaveis/indicadores/volume/V0024_VWAP_of_Obv.txt)**
  Indicador que plota um oscilador calculado com base no OBV e VWAP.

- **[V0025_VZO](estrategias/exemplos/editaveis/indicadores/volume/V0025_VZO.txt)**
  Indicador que plota o Volume Zone Oscillator (VZO).
- **[V0026_Waddah_Attar_Explosion(WAE)](estrategias/exemplos/editaveis/indicadores/volume/V0026_Waddah_Attar_Explosion(WAE).txt)**
  Indicador que plota um histograma baseado em volume e médias.
- **[V0027_Waddah_Attar_Explosion.V2](estrategias/exemplos/editaveis/indicadores/volume/V0027_Waddah_Attar_Explosion.V2.txt)**
  Indicador que usa MACD e Bandas de Bollinger para rastrear direção e força da tendência.

- **[V0031_WVLB_Weis_Wave_Volume_[LazyBear]](estrategias/exemplos/editaveis/indicadores/volume/V0031_WVLB_Weis_Wave_Volume_[LazyBear].txt)**
  Implementação do indicador 'Weis Wave Volume', que acumula o volume em 'ondas' de alta e de baixa, mostrando a força por trás de cada movimento.

- **[V0036_WWEISSWAVE](estrategias/exemplos/editaveis/indicadores/volume/V0036_WWEISSWAVE.txt)**
  Indicador que plota um histograma calculado sobre detector de topos/fundos ponderado pelo volume.

- **[V0050_Color_Time_Segmented_Volume](estrategias/exemplos/editaveis/indicadores/volume/V0050_Color_Time_Segmented_Volume.txt)**
  Regra de coloração que pinta os candles de acordo com o volume segmentado no tempo.

- **[V0029_WaveWeisHMA](estrategias/exemplos/editaveis/indicadores/volume/V0029_WaveWeisHMA.txt)**
  Indicador que plota um oscilador baseado em agressão de compra e venda acumulados.
- **[V0030_Weis_Double_Obv_Medias](estrategias/exemplos/editaveis/indicadores/volume/V0030_Weis_Double_Obv_Medias.txt)**
  Indicador que plota um oscilador baseado em agressão de compra e venda acumulados ponderados pelo OBV.
'''