'''# Boas Práticas de Programação NTSL

Seguir boas práticas ao desenvolver em NTSL torna o código mais legível, seguro e fácil de manter. Abaixo estão algumas recomendações compiladas a partir da documentação e de exemplos práticos.

## 1. Organização e Clareza

-   **Comente Seu Código:** Use `//` para comentários de linha e `{...}` para blocos. Explique o *porquê* de lógicas complexas, não apenas *o que* elas fazem.
-   **Nomes Descritivos:** Use nomes claros para variáveis e parâmetros. Em vez de `p1`, `m2`, use `PeriodoMediaCurta`, `MediaLonga`, etc.
-   **Estrutura Lógica:** Separe a lógica de saída da lógica de entrada. Sempre verifique se há uma posição aberta e se ela deve ser fechada *antes* de procurar por novas entradas. Isso evita comportamentos inesperados.

## 2. Evite Erros Comuns

-   **Não Sombreie Funções Nativas:** **Nunca** declare uma variável com o mesmo nome de uma função nativa (ex: `Media`, `BuyAtMarket`, `ClosePosition`). Isso sobrescreve a função e causará erros difíceis de diagnosticar. Por exemplo, `var BuyAtMarket: integer;` tornará a função `BuyAtMarket` inutilizável.
-   **Cuidado com a Divisão por Zero:** Ao normalizar dados ou criar osciladores, sempre verifique se o divisor não é zero antes de realizar a operação para evitar a interrupção do script.
-   **Use `:=` para Atribuição:** Lembre-se que a atribuição de valores é feita com `:=` e a comparação com `=`. Trocar os dois é um erro comum.

## 3. Gerenciamento de Estado e Performance

-   **Entenda o Fluxo de Execução:** Lembre-se que seu código roda para cada candle. Em tempo real, ele pode ser re-executado várias vezes no mesmo candle. Evite lógicas que dependam de uma única execução por barra, a menos que você use um controle explícito.
-   **Use `LastBarOnChart` para Ações em Tempo Real:** Se uma ação (como um `Alert`) deve ocorrer apenas no candle mais recente, envolva-a em uma condição `if (LastBarOnChart) then ...`.
-   **Otimize Cálculos Pesados:** Laços (`for`, `while`) que rodam muitas vezes ou cálculos complexos podem deixar a execução lenta, especialmente em modo tick-a-tick. Calcule valores que não mudam dentro do candle fora de laços sempre que possível.
-   **Centralize o Gerenciamento de Estado:** Evite criar funções ou procedimentos que modificam variáveis globais (efeitos colaterais). Essa prática torna o código difícil de depurar. Mantenha a lógica de alteração de estado (como zerar contadores ou atualizar metas) dentro do bloco principal `begin...end`.

## 4. Padrões de Código

-   **Use Constantes para Parâmetros de Indicadores:** Funções de indicadores (ex: `AvgTrueRange`, `Media`) esperam que parâmetros como períodos sejam valores constantes (números literais ou `inputs`). Passar uma variável ou uma expressão matemática (ex: `MeuPeriodo * 2`) pode causar erros de compilação inesperados. Se precisar de um valor calculado, crie um novo `input` para ele.
-   **Use Constantes:** Embora não seja formalmente um tipo, a declaração `const` pode ser usada para definir valores fixos, como no caso da função `Asset`. Para outros valores fixos (como números mágicos), usar variáveis no topo do script ajuda na manutenção.
-   **Prefira Funções Puras:** Abstraia lógicas de cálculo em funções que recebem dados via parâmetros e retornam um resultado. Funções puras (sem acesso a variáveis globais) tornam o código mais modular, testável e legível. Isso torna o bloco principal `begin...end` mais limpo, focando na estratégia e no gerenciamento de estado.
'''