
# 📊 Estratégias de Day Trade (Baixo Risco + Alto Retorno)

Este documento reúne as principais estratégias de **Day Trade** extraídas e combinadas do catálogo, 
com foco em operações assertivas e gestão de risco inteligente.

---

## 🔹 1. Day Trade Clássico – Larry Williams
- **Base:** [docs/catalog.md]`STP0003_Trade_e_Acoes_Setup_Larry_Williams_Classico`
- **Confirmação:** [docs/catalog.md]`Rainbow_Charts_4` (tendência pelas médias).
- **Saídas:** Stop curto, alvo fixo (2:1 risco/retorno).
- **Risco:** Médio.
- **Retorno esperado:** Consistente em tendências intraday.
- **Indicação:** WIN, WDO.

---

## 🔹 2. Stormer 901 – Alta Frequência
- **Base:** [docs/catalog.md]`V0061_STORMER_901`
- **Confirmação:** [docs/catalog.md]`TTM_Squeeze` + [docs/catalog.md]`Better_Volume`.
- **Saídas:** Alvos curtos, diversas operações no dia.
- **Risco:** Alto.
- **Retorno esperado:** Alto em movimentos curtos.
- **Indicação:** Mini contratos com forte volatilidade.

---

## 🔹 3. Primeira Barra do Dia
- **Base:** [docs/catalog.md]`V0045_Setup_Primeira_Barra`
- **Confirmação:** [docs/catalog.md]`VWAP` como filtro de fluxo.
- **Saídas:** Stop na barra oposta, alvo curto.
- **Risco:** Médio.
- **Retorno esperado:** Bom aproveitamento da abertura.
- **Indicação:** Gap de abertura ou forte volume inicial.

---

## 🔹 4. Rompimento de Bandas + Volume
- **Base:** [docs/catalog.md]`BollingerBreakout`
- **Confirmação:** [docs/catalog.md]`Volume_Flow_Indicator` ou [docs/catalog.md]`WaveTrend_Oscillator`.
- **Saídas:** Stop na banda contrária, alvo fixo ou móvel.
- **Risco:** Médio-alto.
- **Retorno esperado:** Alto em rompimentos genuínos.
- **Indicação:** Consolidação pré-abertura buscando explosão.

---

## 🔹 5. Scalping Controlado
- **Base:** [docs/catalog.md]`KASTR_SCALP_12R`
- **Confirmação:** [docs/catalog.md]`VWAP` + [docs/catalog.md]`SmartBar` (filtro de fluxo).
- **Saídas:** Scalps de 5 a 10 pontos no mini-dólar ou mini-índice.
- **Risco:** Alto (exige disciplina).
- **Retorno esperado:** Pequenos ganhos recorrentes acumulados.
- **Indicação:** Mercado com liquidez alta e movimentos rápidos.

---

## 🔹 6. Combo Tendência Rápida
- **Base:** [docs/catalog.md]`STP0006_Trade_e_Acoes_Setup_9_1_Larry_Wiilians`
- **Confirmação:** [docs/catalog.md]`HiLo Activator` ou [docs/catalog.md]`SuperTrend`.
- **Saídas:** Stop na mínima/máxima anterior, alvo 2x o risco.
- **Risco:** Médio.
- **Retorno esperado:** Captura movimentos direcionais logo após rompimentos.
- **Indicação:** Mercado já em tendência definida.

---

# 📊 Portfólios Recomendados

### Perfil Conservador (baixo risco)
- 50% Larry Williams (STP0003)
- 30% Primeira Barra (V0045)
- 20% Reversão adaptada intraday (Pisani_Stocastic)

### Perfil Moderado (equilibrado)
- 40% Larry Williams (STP0003)
- 30% Primeira Barra (V0045)
- 30% BollingerBreakout

### Perfil Agressivo (alta frequência)
- 40% Stormer 901 (V0061)
- 40% KASTR Scalping
- 20% Larry Williams (STP0003)

---

🔑 **Observação:** Cada estratégia deve ser testada em simulação antes da execução real. 
A combinação das abordagens visa reduzir risco e aumentar consistência no Day Trade.
