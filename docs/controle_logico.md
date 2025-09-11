'''# Estruturas de Controle e Lógica em NTSL

As instruções de controle de fluxo são utilizadas para administrar a sequência em que os comandos de um script são executados.

## 1. Condicionais: `if ... then ... else`

A estrutura `if` (ou `Se`) permite executar blocos de código apenas se uma determinada condição for verdadeira.

**Sintaxe:**

```ntsl
if (condicao) then
  // código a ser executado se a condição for verdadeira
else
  // código a ser executado se a condição for falsa (opcional)
```

**Uso de `begin` e `end`**

Quando um bloco `then` ou `else` precisa conter múltiplas instruções, ele deve ser delimitado pelas palavras-chave `begin` e `end`. As palavras `inicio` e `fim` podem ser usadas como sinônimos.

**Exemplo:**

```ntsl
begin
  if (Close > Media(20, Close)) then
  begin
    PaintBar(clGreen); // Múltiplas instruções
    PlotText('Acima da Média', clGreen);
  end
  else
  begin
    PaintBar(clRed);
    PlotText('Abaixo da Média', clRed);
  end;
end;
```

## 2. Laços de Repetição

### `for`

O laço `for` (ou `Para`) é usado para executar um bloco de código um número específico de vezes.

-   `for i := 0 to 10 do ...` (incrementa a variável `i`)
-   `for i := 10 downto 0 do ...` (decrementa a variável `i`)

**Exemplo:**

```ntsl
var
  soma: float;
  i: integer;
begin
  soma := 0;
  for i := 0 to 9 do
  begin
    soma := soma + Close[i];
  end;
  Plot(soma / 10);
end;
```

### `while`

O laço `while` (ou `Enquanto`) executa um bloco de código enquanto uma condição for verdadeira. A condição é testada **antes** da primeira execução.

**Exemplo:**

```ntsl
var
  contador: integer;
begin
  contador := 0;
  while (contador < 5) do
  begin
    // este bloco executará 5 vezes
    contador := contador + 1;
  end;
end;
```

### `repeat ... until`

Similar ao `while`, mas a condição é testada **após** a execução do bloco. Isso garante que o código seja executado pelo menos uma vez.

**Exemplo:**

```ntsl
var
  contador: integer;
begin
  contador := 0;
  repeat
    contador := contador + 1;
  until (contador >= 5);
end;
```

## 3. Operadores Lógicos

Para criar condições complexas, utilize os operadores lógicos:

-   `and` (E): Ambas as condições devem ser verdadeiras.
-   `or` (OU): Pelo menos uma das condições deve ser verdadeira.
-   `not` (NÃO): Inverte o resultado da condição.

**Exemplo:**

```ntsl
if (Close > Media(20, Close)) and (Volume > 100000) then
  PaintBar(clGreen);
```
'''