'''# Sintaxe da Linguagem NTSL

Esta seção detalha as regras de sintaxe e os padrões estruturais para escrever scripts na Nelogica Trading System Language (NTSL).

## 1. Estrutura Básica de um Script

Um script NTSL é sempre dividido em três áreas principais, nesta ordem:

1.  **Parâmetros de Entrada (`input`):** Define as variáveis que o usuário pode configurar pela interface da plataforma.
2.  **Variáveis e Funções (`var`):** Declaração de variáveis globais e criação de funções (`function`) ou procedimentos (`procedure`) personalizados.
3.  **Código Principal (`begin`...`end`):** Contém a lógica principal da estratégia.

**Nota:** Os blocos `input` e `var` são declarados apenas uma vez no início do arquivo. As palavras-chave `inicio` e `fim` são sinônimos diretos de `begin` e `end`.

**Exemplo de Estrutura:**

```ntsl
input
  PeriodoMedia(20);
  FonteDados(Close);

var
  mediaCalculada: float;

begin
  mediaCalculada := Media(PeriodoMedia, FonteDados);
  Plot(mediaCalculada);
end;
```

## 2. Comentários

-   **Comentário de Linha Única:** Use `//`.
-   **Comentário de Múltiplas Linhas:** Envolva o texto com chaves `{` e `}`.

**Exemplo:**

```ntsl
// Esta é uma linha de comentário
{ 
  Este é um comentário
  de múltiplas linhas.
}
```

## 3. Declarações e Literais

Todas as declarações de parâmetros e variáveis devem ser terminadas com um ponto e vírgula (`;`).

-   **Parâmetros (`input`):** `NomeDoParametro(ValorPadrao);`
-   **Variáveis (`var`):** `NomeDaVariavel: Tipo;`
-   **Strings:** Literais de texto devem ser sempre delimitados por **aspas duplas** (`"`). O uso de aspas simples (`'`) não é suportado e causará erros de compilação.

## 4. Operadores

-   **Atribuição:** `:=`
-   **Comparação:** `=`, `<>` (diferente), `>`, `<`, `>=`, `<=`
-   **Aritméticos:** `+`, `-`, `*`, `/` (divisão de ponto flutuante). O operador `div` para divisão inteira existe mas é raramente utilizado.
-   **Lógicos:** `and`, `or`, `not`

## 5. Sintaxe Avançada: Acesso a Linhas de Indicadores (`|n|`)

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

## 6. Funções e Procedimentos

A sintaxe para declarar funções e procedimentos é estrita e segue o padrão Pascal.

-   **Declaração:** Funções e procedimentos devem ser declarados na área `var`, antes do bloco principal `begin...end`.
-   **Variáveis Locais:** Variáveis específicas para uma função/procedimento devem ser declaradas em um bloco `var` próprio, localizado *entre* a assinatura da função e o seu `begin`.

**Sintaxe de Função com Variáveis Locais:**

```ntsl
function NomeDaFuncao(parametro1: Tipo): TipoDeRetorno;
var
  variavelLocal: Tipo;
begin
  // Lógica da função...
  Result := valorDeRetorno;
end;
```

**Sintaxe de Procedimento com Variáveis Locais:**

```ntsl
procedure NomeDoProcedimento(parametro1: Tipo);
var
  outraVariavel: Tipo;
begin
  // Ações do procedimento...
end;
```

Colocar o bloco `var` local dentro do `begin...end` da função é um erro de sintaxe comum e deve ser evitado.

## 6. Funções e Procedimentos

A sintaxe para declarar funções e procedimentos é estrita e segue o padrão Pascal.

-   **Declaração:** Funções e procedimentos devem ser declarados na área `var`, antes do bloco principal `begin...end`.
-   **Variáveis Locais:** Variáveis específicas para uma função/procedimento devem ser declaradas em um bloco `var` próprio, localizado *entre* a assinatura da função e o seu `begin`.

**Sintaxe de Função com Variáveis Locais:**

```ntsl
function NomeDaFuncao(parametro1: Tipo): TipoDeRetorno;
var
  variavelLocal: Tipo;
begin
  // Lógica da função...
  Result := valorDeRetorno;
end;
```

**Sintaxe de Procedimento com Variáveis Locais:**

```ntsl
procedure NomeDoProcedimento(parametro1: Tipo);
var
  outraVariavel: Tipo;
begin
  // Ações do procedimento...
end;
```

Colocar o bloco `var` local dentro do `begin...end` da função é um erro de sintaxe comum e deve ser evitado.
'''