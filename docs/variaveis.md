'''# Variáveis e Tipos de Dados em NTSL

Esta seção detalha os tipos de dados, o escopo das variáveis e os padrões para manipulação de dados em NTSL.

## 1. Área de Declaração (`var`)

Todas as variáveis e funções customizadas são declaradas em um único bloco `var`, que fica entre o bloco `input` e o bloco principal `begin`.

**Sintaxe:**

```ntsl
var
  NomeDaVariavel1: Tipo;
  NomeDaVariavel2: Float;
```

**Escopo:** Todas as variáveis declaradas no bloco `var` são globais. Seus valores persistem entre as execuções do script em cada candle, a menos que sejam redefinidas. Variáveis do tipo `Serie` são uma exceção, pois seus valores são zerados a cada novo candle.

## 2. Tipos de Dados

-   **Float ou Real:** Para números de ponto flutuante (decimais).
-   **Integer ou Inteiro:** Para números inteiros.
-   **Boolean ou Booleano:** Para valores lógicos `True` ou `False`.
-   **String:** Para textos. Usado em funções como `PlotText`.
-   **Serie:** Representa uma série de dados históricos, como preços de fechamento (`Close`) ou os valores de um indicador.

## 3. Séries de Dados (`Serie`)

Séries são a base da NTSL e representam dados históricos. As séries nativas mais comuns são:

-   `Close` ou `Fechamento`
-   `Open` ou `Abertura`
-   `High` ou `Maxima`
-   `Low` ou `Minima`
-   `Volume`
-   `Quantity` ou `Quantidade`

Para acessar valores passados de uma série, usa-se a sintaxe de colchetes `[n]`, onde `n` é o número de candles no passado. `Close[0]` é o fechamento do candle atual, `Close[1]` é o do candle anterior, e assim por diante.

## 4. Acessando Múltiplas Linhas de um Indicador (Sintaxe `|n|`)

Um padrão crucial para indicadores que retornam múltiplos valores (como Bandas de Bollinger ou MACD) é o uso do operador `|n|` para acessar as diferentes linhas de dados. A contagem começa em `0`.

**Exemplo com Bandas de Bollinger:**

```ntsl
var
  BandaSuperior, BandaInferior: float;
begin
  // Acessa a primeira linha (banda superior)
  BandaSuperior := BollingerBands(2.0, 20, 0)|0|;

  // Acessa a segunda linha (banda inferior)
  BandaInferior := BollingerBands(2.0, 20, 0)|1|;

  Plot(BandaSuperior);
  Plot2(BandaInferior);
end;
```

**Exemplo com MACD:**

```ntsl
var
  LinhaMACD, LinhaSinal: float;
begin
  // Acessa a linha principal do MACD
  LinhaMACD := MACD(26, 12, 9)|0|;

  // Acessa a linha de sinal
  LinhaSinal := MACD(26, 12, 9)|1|;

  Plot(LinhaMACD);
  Plot2(LinhaSinal);
end;
```

## 5. Arrays

Arrays são coleções de tamanho fixo de um tipo de dado específico. São úteis para armazenar um conjunto limitado de valores.

**Sintaxe de Declaração:**

```ntsl
var
  minhaLista: array[1..10] of Integer;
```

## 6. Sombreamento de Funções (Boas Práticas)

Declarar uma variável com o mesmo nome de uma função nativa (ex: `BuyAtMarket`, `Media`) fará com que a função original se torne inacessível, gerando erros. **Evite sempre usar nomes de funções nativas para suas variáveis.**

## 7. Escopo de Variáveis (Global vs. Local)

Compreender o escopo é vital para evitar erros.

-   **Variáveis Globais:** Declaradas no bloco `var` principal, no início do script. Elas são acessíveis de qualquer parte do código, incluindo dentro de funções e procedimentos. Seus valores persistem entre as execuções do script em cada candle.

-   **Variáveis Locais:** Declaradas em um bloco `var` dentro de uma função ou procedimento. Elas **só existem e só podem ser acessadas dentro daquela função ou procedimento**. Seus valores são reiniciados a cada chamada.

**Exemplo:**

```ntsl
var
  variavelGlobal: Integer; // Global

procedure MeuProcedimento;
var
  variavelLocal: Integer; // Local
begin
  // ERRADO: Acessar/modificar globais dentro de sub-rotinas é má prática.
  // variavelGlobal := 10; 
  
  variavelLocal := 5;   // CORRETO: Modificar uma local.
end;

begin // Bloco Principal
  variavelGlobal := 1; // CORRETO: Modificar globais no escopo principal.
  // variavelLocal := 2; // INVÁLIDO! Geraria um erro de compilação.
  
  MeuProcedimento();
end;
```

**Recomendação:** Evite modificar variáveis globais diretamente de dentro de funções ou procedimentos. Esta prática é considerada um "efeito colateral" (side effect) e pode tornar o código difícil de entender e depurar. Prefira que funções retornem um valor e que a lógica de alteração de estado fique centralizada no bloco principal `begin...end`.

## 7. Escopo de Variáveis (Global vs. Local)

Compreender o escopo é vital para evitar erros.

-   **Variáveis Globais:** Declaradas no bloco `var` principal, no início do script. Elas são acessíveis de qualquer parte do código, incluindo dentro de funções e procedimentos. Seus valores persistem entre as execuções do script em cada candle.

-   **Variáveis Locais:** Declaradas em um bloco `var` dentro de uma função ou procedimento. Elas **só existem e só podem ser acessadas dentro daquela função ou procedimento**. Seus valores são reiniciados a cada chamada.

**Exemplo:**

```ntsl
var
  variavelGlobal: Integer; // Global

procedure MeuProcedimento;
var
  variavelLocal: Integer; // Local
begin
  variavelGlobal := 10; // Válido: pode modificar uma global
  variavelLocal := 5;   // Válido: pode modificar uma local
end;

begin // Bloco Principal
  variavelGlobal := 1; // Válido
  // variavelLocal := 2; // INVÁLIDO! Geraria um erro de compilação.
  
  MeuProcedimento();
end;
```

**Recomendação:** Evite modificar variáveis globais diretamente de dentro de funções ou procedimentos. Esta prática é considerada um "efeito colateral" (side effect) e pode tornar o código difícil de entender e depurar. Prefira que funções retornem um valor e que a lógica de alteração de estado fique centralizada no bloco principal `begin...end`.
'''