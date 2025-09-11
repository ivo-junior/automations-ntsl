'''# Funções de Ordem e Gerenciamento de Posição

Esta seção aborda as funções utilizadas para enviar ordens de compra, venda e para gerenciar posições abertas em NTSL.

## 1. Tipos de Ordens

Existem dois tipos principais de ordens de mercado em NTSL:

*   **Ordens de Entrada:** Usadas para iniciar uma nova posição (comprada ou vendida).
*   **Ordens de Saída (Cobertura):** Usadas para fechar uma posição existente.

É crucial usar o tipo de ordem correto para evitar lógicas inesperadas. Por exemplo, usar `BuyAtMarket` quando já se está comprado não terá efeito, mas usá-la quando se está vendido irá fechar a posição de venda (e não abrir uma nova posição de compra, a menos que a quantidade seja maior que a posição vendida).

### Funções de Entrada

-   `BuyAtMarket`: Envia uma ordem de compra a mercado.
-   `SellShortAtMarket`: Envia uma ordem de venda a descoberto a mercado.
-   `BuyStop` / `BuyLimit`: Enviam ordens de compra pendentes.
-   `SellShortStop` / `SellShortLimit`: Enviam ordens de venda pendentes.

### Funções de Saída (Cobertura)

-   `SellToCoverAtMarket`: Envia uma ordem de venda para zerar uma posição comprada.
-   `BuyToCoverAtMarket`: Envia uma ordem de compra para zerar uma posição vendida.
-   `ClosePosition`: Envia uma ordem a mercado para zerar qualquer posição em aberto, seja ela comprada ou vendida. É uma forma segura e genérica de sair do mercado.

## 2. Padrão de Estrutura Lógica para Trading

A forma mais segura e comum de estruturar uma estratégia é verificar primeiro o estado da posição atual e tratar as saídas antes de procurar por novas entradas.

**Exemplo de Estrutura Lógica:**

```ntsl
begin
  // ====================================================
  //  1. GERENCIAMENTO DE POSIÇÃO (LÓGICA DE SAÍDA)
  // ====================================================
  if (IsBought) then // Se estiver comprado
  begin
    // Exemplo: Sair se o preço cruzar abaixo da média
    if (Close < Media(20, Close)) then
      SellToCoverAtMarket; // Zera a posição de compra
  end
  else if (IsSold) then // Se estiver vendido
  begin
    // Exemplo: Sair se o preço cruzar acima da média
    if (Close > Media(20, Close)) then
      BuyToCoverAtMarket; // Zera a posição de venda
  end;

  // ====================================================
  //  2. LÓGICA DE ENTRADA
  // ====================================================
  // Só executa se não houver nenhuma posição em aberto
  if (HasPosition = false) then
  begin
    // Exemplo: Entrar comprado se o preço cruzar acima da média longa
    if (Close > Media(50, Close)) then
      BuyAtMarket;
    // Exemplo: Entrar vendido se o preço cruzar abaixo da média longa
    else if (Close < Media(50, Close)) then
      SellShortAtMarket;
  end;
end;
```
'''