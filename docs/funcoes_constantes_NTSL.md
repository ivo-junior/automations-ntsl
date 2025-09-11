# Mapa de Funções e Constantes NTSL

Este documento serve como uma referência rápida para todas as funções e constantes disponíveis na linguagem NTSL, compilado a partir do manual oficial.

## Constantes

### Lado da Ordem (`os...`)
- **osCompra**: Representa uma ordem de compra.
- **osVenda**: Representa uma ordem de venda.

### Tipo de Opção (`opt...`)
- **optCall**: Opção de compra (Call).
- **optPut**: Opção de venda (Put).

### Tipo de Ordem (`ot...`)
- **otLimit**: Ordem do tipo Limite.
- **otMarket**: Ordem do tipo A Mercado.
- **otStopLimit**: Ordem do tipo Stop.

### Cores (`cl...`)
- **clAqua / clAzulClaro**: Cor azul-claro.
- **clBlack / clPreto**: Cor preta.
- **clBlue / clAzul**: Cor azul.
- **clCream / clCreme**: Cor creme.
- **clDarkGray / clCinzaEscuro**: Cor cinza-escuro.
- **clFuchsia / clFucsia**: Cor fúcsia.
- **clGray / clCinza**: Cor cinza.
- **clGreen / clVerde**: Cor verde.
- **clLime / clVerdeLimao**: Cor verde-limão.
- **clLightGray / clCinzaClaro**: Cor cinza-claro.
- **clMaroon / clMarrom**: Cor marrom.
- **clMediumGray / clCinzaMedio**: Cor cinza médio.
- **clLightGreen / clVerdeClaro**: Cor verde-claro.
- **clNavy / clAzulMarinho**: Cor azul-marinho.
- **clOlive / clVerdeOliva**: Cor verde-oliva.
- **clPurple / clPurpura**: Cor púrpura.
- **clRed / clVermelho**: Cor vermelha.
- **clSilver / clPrata**: Cor prata.
- **clTeal**: Cor verde-azulado.
- **clWhite / clBranco**: Cor branca.
- **clYellow / clAmarelo**: Cor amarela.

### Constantes Matemáticas (`Math_...`)
- **Math_PI**: Número Pi (π).
- **Math_Sqrt2**: Raiz quadrada de 2.
- **Math_Euler**: Número de Euler (e).
- **E outras...**: O manual lista diversas outras constantes matemáticas para cálculos avançados.

### Feeds de Bolsas (`feed...`)
- **feedBMF**: Bolsa de Mercadorias & Futuros.
- **feedBovespa**: Bolsa de Valores de São Paulo.
- **feedCME**: Chicago Mercantile Exchange.
- **E outras...**: `feedBCB`, `feedDowJones`, `feedNasdaq`, `feedNyse`, etc.

---

## Funções por Categoria

### 13. Funções de Alarme
- **Alert(`Color: Integer`)**: Gera um alarme visual com um popup na cor especificada.

### 14. Funções de Back-Testing (Ordens e Posição)
- **BuyAtMarket(`Quantity: Float`)**: Envia uma ordem de compra a mercado.
- **BuyLimit(`Limit: Float; Quantity: Float`)**: Envia uma ordem de compra limitada.
- **BuyStop(`Stop: Float; Limit: Float; Quantity: Float`)**: Envia uma ordem de compra stop.
- **SellShortAtMarket(`Quantity: Float`)**: Envia uma ordem de venda a descoberto a mercado.
- **SellShortLimit(`Limit: Float; Quantity: Float`)**: Envia uma ordem de venda a descoberto limitada.
- **SellShortStop(`Stop: Float; Limit: Float; Quantity: Float`)**: Envia uma ordem de venda a descoberto stop.
- **BuyToCoverAtMarket(`Quantity: Float`)**: Zera uma posição vendida com uma ordem a mercado.
- **BuyToCoverLimit(`Limit: Float; Quantity: Float`)**: Zera uma posição vendida com uma ordem limitada.
- **BuyToCoverStop(`Stop: Float; Limit: Float; Quantity: Float`)**: Zera uma posição vendida com uma ordem stop.
- **SellToCoverAtMarket(`Quantity: Float`)**: Zera uma posição comprada com uma ordem a mercado.
- **SellToCoverLimit(`Limit: Float; Quantity: Float`)**: Zera uma posição comprada com uma ordem limitada.
- **SellToCoverStop(`Stop: Float; Limit: Float; Quantity: Float`)**: Zera uma posição comprada com uma ordem stop.
- **ClosePosition()**: Envia uma ordem a mercado para zerar qualquer posição aberta.
- **ReversePosition()**: Inverte a posição atual (de compra para venda ou vice-versa).
- **CancelPendingOrders()**: Cancela todas as ordens pendentes.
- **SendOrder(`Side`, `Type`, `Quantity`, `Limit`, `Stop`)**: Envia uma ordem customizada.
- **Position()**: Retorna o tamanho da posição em lotes (positivo para compra, negativo para venda).
- **PositionQty()**: Retorna o tamanho da posição em quantidade.
- **BuyPosition() / SellPosition()**: Retorna o tamanho da posição de compra ou venda em lotes.
- **BuyPrice() / SellPrice()**: Retorna o preço médio da posição de compra ou venda.
- **HasPosition()**: Retorna `True` se houver alguma posição aberta.
- **IsBought() / IsSold()**: Retorna `True` se a posição atual for comprada ou vendida, respectivamente.
- **DailyResult(`OpenResult: Boolean`)**: Retorna o resultado financeiro do dia (aberto + fechado ou apenas fechado).
- **OpenResult()**: Retorna o resultado financeiro da posição atualmente em aberto.

### 15. Funções de Calendário e Tempo
- **Date()**: Retorna a data do candle atual (`1AnoMêsDia`).
- **Time()**: Retorna a hora de abertura do candle atual (`HHMM`).
- **CurrentDate() / CurrentTime()**: Retorna a data/hora atual do sistema.
- **DayOfWeek(`Date`)**: Retorna o dia da semana para a data especificada.
- **CloseD(`DaysAgo`) / OpenD / HighD / LowD**: Retorna o Fechamento/Abertura/Máxima/Mínima de N dias atrás.
- **CloseW / OpenW / HighW / LowW**: O mesmo para semanas.
- **CloseM / OpenM / HighM / LowM**: O mesmo para meses.
- **CloseY / OpenY / HighY / LowY**: O mesmo para anos.
- **FindBar(`TargetDate`, `TargetTime`)**: Retorna o índice de uma barra específica.
- **LastBarOnChart()**: Retorna `True` se o candle atual for o último do gráfico.

### 18. Funções Gráficas
- **Plot() / Plot2() ... Plot99()**: Desenha uma linha no gráfico do indicador.
- **PlotN(`PlotNum`, `Valor`)**: Desenha uma linha em um plot específico.
- **PaintBar(`Cor`)**: Colore a barra/candle do gráfico principal.
- **PlotText(`Content`, `Color`, `Position`, ...)**: Escreve um texto no gráfico.
- **HorizontalLine(`Y`, `Color`)**: Desenha uma linha horizontal.
- **RGB(`Red`, `Green`, `Blue`)**: Cria uma cor customizada.
- **SetPlotColor / SetPlotWidth / SetPlotStyle**: Customiza a aparência de um plot.
- **Range()**: Retorna a diferença entre a máxima e a mínima do candle.
- **TrueRange()**: Retorna o "range verdadeiro".

### 19. Indicadores (Seleção)
- **ADX(`Periodo`, `Media`)**: Average Directional Index.
- **AccAgressSaldo(`Tipo`)**: Acúmulo de Agressão - Saldo.
- **AvgTrueRange(`Periodo`, `Tipo`)**: Média do True Range.
- **BollingerBands(`Desvio`, `Periodo`, `Tipo`)**: Bandas de Bollinger. Retorna múltiplas linhas (`|0|` para superior, `|1|` para inferior).
- **CCI(`Periodo`)**: Commodity Channel Index.
- **DiPDiM(`Periodo`)**: Indicador Direcional (DI+ e DI-). Retorna múltiplas linhas (`|0|` para DI+, `|1|` para DI-).
- **HiLoActivator(`Periodo`)**: HiLo Activator.
- **MACD(`MediaLonga`, `MediaCurta`, `Sinal`)**: Moving Average Convergence Divergence. Retorna múltiplas linhas (`|0|` para linha MACD, `|1|` para Histograma).
- **Media(`Periodo`, `TipoSerie`)**: Média Móvel Aritmética.
- **MediaExp(`Periodo`, `Dados`)**: Média Móvel Exponencial.
- **OBV()**: On-Balance Volume.
- **RSI(`Periodo`, `Tipo`)**: Relative Strength Index (Índice de Força Relativa).
- **StopATR(`Desvio`, `Periodo`, `Tipo`)**: Stop ATR.
- **TopBottomDetector(`Periodo`)**: Detector de Topos e Fundos.
- **VWAP(`Periodo`)**: Volume Weighted Average Price (Preço Médio Ponderado por Volume).

### 21. Funções Matemáticas (Seleção)
- **ABS(`Valor`)**: Retorna o valor absoluto.
- **Floor(`Num`)**: Arredonda para o maior inteiro menor ou igual ao número.
- **Round(`Valor`)**: Arredonda para o inteiro mais próximo.
- **Sqrt(`Valor`)**: Retorna a raiz quadrada.
- **Power(`Valor`, `Potencia`)**: Retorna a potência de um número.

### 24. Funções de Usuário (Seleção)
- **Highest(`Serie`, `Periodo`)**: Retorna o maior valor de uma série em um período.
- **Lowest(`Serie`, `Periodo`)**: Retorna o menor valor de uma série em um período.
- **Summation(`Serie`, `Periodo`)**: Retorna a soma dos valores de uma série em um período.
- **WAverage(`Serie`, `Periodo`)**: Média Ponderada.
