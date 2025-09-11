'''# Exemplos Práticos de Código NTSL

A melhor forma de aprender uma linguagem é através de exemplos práticos. Abaixo estão três scripts completos que demonstram os principais casos de uso da NTSL: um indicador, uma regra de coloração e uma estratégia de execução.

## 1. Indicador Simples: Média Móvel Exponencial

Este script calcula e plota uma média móvel exponencial no gráfico.

```ntsl
// Define o parâmetro que o usuário pode alterar na interface
input
  Periodo(21);

// Declara uma variável para armazenar o resultado do cálculo
var
  mediaCalculada: float;

begin
  // Calcula a média móvel exponencial usando a função nativa MediaExp
  mediaCalculada := MediaExp(Periodo, Close); 

  // Plota o resultado no gráfico
  Plot(mediaCalculada);
end;
```

## 2. Regra de Coloração: Cruzamento de Médias

Este script colore as barras do gráfico com base no cruzamento de duas médias móveis: uma rápida e uma lenta.

```ntsl
input
  PeriodoCurto(9);
  PeriodoLongo(21);

var
  mediaCurta, mediaLonga: float;

begin
  // Calcula as duas médias
  mediaCurta := MediaExp(PeriodoCurto, Close);
  mediaLonga := MediaExp(PeriodoLongo, Close);

  // Lógica condicional para colorir as barras
  if (mediaCurta > mediaLonga) then
    PaintBar(clGreen) // Tendência de alta
  else
    PaintBar(clRed);  // Tendência de baixa
end;
```

## 3. Estratégia de Execução: Robô de Cruzamento de Médias

Este script implementa um robô de negociação simples que compra e vende com base no cruzamento das médias, seguindo as boas práticas de gerenciamento de posição.

```ntsl
input
  MediaCurtaPeriodo(9);
  MediaLongaPeriodo(21);

var
  mediaCurta, mediaLonga: float;

begin
  // --- 1. Calcula os indicadores ---
  mediaCurta := MediaExp(MediaCurtaPeriodo, Close);
  mediaLonga := MediaExp(MediaLongaPeriodo, Close);

  // --- 2. Lógica de Saída (se posicionado) ---
  if (IsBought) then // Se estiver comprado...
  begin
    // ...e a média curta cruzar para baixo da longa, zera a posição.
    if (mediaCurta < mediaLonga) then
      SellToCoverAtMarket;
  end
  else if (IsSold) then // Se estiver vendido...
  begin
    // ...e a média curta cruzar para cima da longa, zera a posição.
    if (mediaCurta > mediaLonga) then
      BuyToCoverAtMarket;
  end;

  // --- 3. Lógica de Entrada (se não estiver posicionado) ---
  if (HasPosition = false) then
  begin
    // Se a média curta cruzar para cima da longa, compra.
    if (mediaCurta > mediaLonga) and (mediaCurta[1] <= mediaLonga[1]) then
      BuyAtMarket;
    // Se a média curta cruzar para baixo da longa, vende.
    else if (mediaCurta < mediaLonga) and (mediaCurta[1] >= mediaLonga[1]) then
      SellShortAtMarket;
  end;
end;
```
'''