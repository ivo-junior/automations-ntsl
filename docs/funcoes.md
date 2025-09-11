'''# Funções e Procedimentos em NTSL

Esta seção descreve como criar e utilizar funções e procedimentos, além de listar as funções nativas disponíveis na plataforma.

## 1. Padrões Comuns de Uso de Funções

A análise de exemplos práticos revela uma estrutura lógica comum para a criação de estratégias de negociação. A abordagem mais segura é sempre verificar as condições de saída de uma posição existente antes de avaliar novas oportunidades de entrada.

**Exemplo de Estrutura Lógica para Trading:**

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
  // S executa se no houver nenhuma posio em aberto
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

## 2. Criando Funções e Procedimentos

Para organizar e reutilizar código, NTSL permite a criação de funções e procedimentos. A declaração deve ser feita na área `var`, antes do bloco de código principal.

-   **Função (`function`):** Um bloco de código que recebe parâmetros e **retorna um valor**. Ideal para cálculos que precisam ser reutilizados, como a lógica de um sinal. Funções devem ser "puras" sempre que possível, ou seja, seus resultados devem depender apenas de seus parâmetros de entrada, sem acessar variáveis globais.

-   **Procedimento (`procedure`):** Um bloco de código que executa uma série de comandos (ações), mas **não retorna um valor**. Útil para agrupar ações (ex: `PaintBar`). **É uma má prática criar procedimentos que modificam o estado global do robô**. Lógicas que precisam alterar variáveis globais devem ser mantidas dentro do bloco principal `begin...end` para maior clareza e controle do fluxo de dados.

### Sintaxe e Boas Práticas

A estrutura correta é fundamental. Variáveis locais devem ser declaradas em um bloco `var` próprio, posicionado **antes** do `begin` da função ou procedimento.

**Sintaxe de Função (Prática Recomendada):**

```ntsl
function MinhaFuncaoCalculaMedia(pPeriodo: Integer; pFonte: Serie): Float;
var
  mediaCalculada: Float; // Variável local
begin
  mediaCalculada := Media(pPeriodo, pFonte);
  Result := mediaCalculada; // Retorna o valor usando a palavra-chave 'Result'
end;
```

**Sintaxe de Procedimento (para Ações):**

```ntsl
procedure PintaCandle(pCondicao: Boolean);
var
  cor: Integer; // Variável local
begin
  if (pCondicao) then
    cor := clGreen
  else
    cor := clRed;
  
  PaintBar(cor); // Executa uma ação sem retorno
end;
```

**Boas Práticas:**

1.  **Passe Parâmetros:** Em vez de acessar diretamente variáveis de `input` ou `var` globais, passe-as como parâmetros para suas funções. Isso torna o código mais legível, modular e fácil de testar.
2.  **Use Funções Puras para Cálculos:** Isole lógicas de cálculo complexas em funções. O bloco principal do seu código ficará mais limpo, focando na estratégia de negociação.
3.  **Evite Procedimentos com Efeitos Colaterais:** Não crie procedimentos para modificar variáveis globais. Esta prática pode levar a um código difícil de depurar. Mantenha a lógica de gerenciamento de estado centralizada no bloco `begin...end`.

## 3. Lista de Funções Nativas

(A lista de funções do manual original continua aqui como referência)

- 13 Funções de Alarme
- 14 Funções de Back-Testing
- 15 Funções de Calendário
- 16 Funções de Candlestick
- 18 Funções Gráficas
- 19 Indicadores
- 20 Funções de Livro
- 21 Funções Matemáticas
- 22 Funções de Opções
- 24 Funções de Usuário
- 25 Funções Utilitárias
'''