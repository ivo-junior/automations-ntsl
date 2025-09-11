'''# Fluxo de Execução em NTSL

Compreender o fluxo de execução é fundamental para criar estratégias que se comportem como o esperado tanto em backtests quanto em tempo real.

## 1. O Loop de Execução por Candle

A lógica principal de um script NTSL (o bloco `begin...end`) não é executada apenas uma vez. Ela opera dentro de um loop implícito que percorre, um por um, todos os candles (barras) do gráfico, do mais antigo ao mais recente.

-   Para cada candle do histórico, o script é executado uma vez.
-   No candle atual (em tempo real), o script é re-executado a cada novo tick (negócio) que chega do mercado.

**Importante:** Dentro do código, `Close`, `High`, `Low`, etc., sempre se referem aos dados do candle que está sendo processado no momento, não necessariamente o último candle do gráfico.

## 2. Reprocessamento de Candles

Um mesmo candle pode ser processado várias vezes. Este é um conceito crucial.

**Principais gatilhos para reprocessamento:**

-   **Novos Ticks:** Em tempo real, cada novo negócio no ativo faz com que o script re-execute no candle atual.
-   **Execução de Ordens:** Quando uma ordem de entrada é executada, o fluxo de execução reprocessa o mesmo candle imediatamente para permitir que a lógica de saída (ordens de cobertura como `SellToCoverAtMarket`) seja ativada e proteja a nova posição.
-   **Recálculo de Indicadores:** Alguns indicadores podem, em raras ocasiões, alterar seus valores em candles passados, forçando um reprocessamento em cascata até o candle atual.

Devido a esse comportamento, variáveis globais devem ser usadas com cuidado, pois seu valor pode ser alterado várias vezes dentro do mesmo candle.

## 3. A Função `LastBarOnChart`

Para garantir que uma parte do código seja executada **apenas** no último candle do gráfico (o que está em formação), pode-se usar a função `LastBarOnChart()`.

**Exemplo:**

```ntsl
begin
  if (LastBarOnChart) then
  begin
    // Este código só será executado em tempo real no candle atual
    Alert(clGreen);
  end;
end;
```

## 4. Modos de Execução (Automação)

O fluxo de execução da sua estratégia pode ser alterado significativamente dependendo do **Modo de Execução** configurado no painel de automação da plataforma:

-   **No Fechamento do Candle:** A lógica de envio de ordens é avaliada apenas uma vez por candle, no momento em que ele fecha. Este modo é o que mais se assemelha ao backtest.
-   **Quando a Condição for Satisfeita:** A lógica é avaliada continuamente, tick a tick. Isso permite entradas e saídas imediatas assim que uma condição é atendida, mesmo no meio de um candle. Este modo oferece mais agilidade, mas seu comportamento não pode ser simulado com precisão no backtest padrão.
'''