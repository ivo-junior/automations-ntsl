
# ⚙️ Blueprint de Automação Composta — Day Trade (WIN/WDO)
**Escopo:** Orquestrar múltiplas estratégias intraday com baixo risco e alto retorno, priorizando execução segura, telemetria e reprodutibilidade (backtest/live).  
**Ativos-alvo:** Mini-Índice (WIN) e Mini-Dólar (WDO).  
**Sessão:** 09:00–17:55 BRT (ajuste conforme regra da corretora).

**OBS**: Dodos esses indicadores e estratégias estão disponíveis no catálogo de exemplos (`docs/catalog.md`).

---

## 1) Arquitetura Lógica (Visão Geral)
- **Módulos de Estratégia (engines):**  
  `STP0003_LarryWilliams`, `V0061_Stormer901`, `V0045_PrimeiraBarra`, `BollingerBreakout`, `KASTR_Scalp_12R`, `STP0006_9_1_Larry`  
- **Orquestrador:**  
  - Coleta sinais dos módulos, aplica **pesos de confiança**, resolve conflitos, deduplica entradas e respeita limites globais (risco, número de trades).  
- **Risk Engine (global):**  
  - Sizing por volatilidade (ATR), `MaxDailyLoss`, `MaxPositions`, `MaxConsecutiveLosses`, **Circuit Breakers** (pausa em eventos).  
- **Gerenciamento de Trade (per position):**  
  - Stops (fixo/volatilidade), alvo parcial, trailing dinâmico, **break-even** e **time-based exit**.  
- **Scheduler/Session Filter:**  
  - Janelas por estratégia (ex.: Primeira Barra somente 09:00–09:20), filtros de **notícias** (se disponível) e horários proibidos.  

---

## 2) Pesos do Orquestrador (Perfilado)
**Conservador**
- 50% STP0003_LarryWilliams
- 30% V0045_PrimeiraBarra
- 20% BollingerBreakout (ou Reversão adaptada)

**Moderado**
- 40% STP0003_LarryWilliams
- 30% V0045_PrimeiraBarra
- 30% BollingerBreakout

**Agressivo (alta frequência)**
- 40% V0061_Stormer901
- 40% KASTR_Scalp_12R
- 20% STP0003_LarryWilliams

> **Regra:** o orquestrador usa o **score** = soma(peso × sinal normalizado) por ativo. Dispara ordem somente se `score >= Threshold` e risco global permitir.

---

## 3) Limites Globais (Risk Engine)
- **Risco por trade:** 0,5–1,0% do capital.  
- **MaxDailyLoss:** 3–5% (ao atingir: **pausa** todas as estratégias).  
- **MaxPositions:** 2 simultâneas por ativo.  
- **MaxConsecutiveLosses:** 3 (ao atingir: pausa 30–60 min ou encerrar o dia).  
- **Slippage Model:** configure por ativo (ex.: 1–2 pts WIN, 0,5–1,0 pts WDO).  
- **Circuit Breakers:** pausa se volatilidade > limiar (ATR em janela curta) ou spreads > X.

---

## 4) Gestão de Posição (Padrão)
- **Stop Inicial:** `max(ATR*k, estrutura técnica)` (k entre 1,2 e 2,0).  
- **Alvos:**  
  - Parcial 1 (50%): 1R  
  - Parcial 2 (50%): 2R (ou trailing via ATR para tentar alongar)  
- **Break-even:** ao atingir 0,8–1,0R, mover stop para preço de entrada.  
- **Trailing:** ATR dinâmico (1,0 a 1,5 × ATR), ou HiLo/Parabolic.  
- **Time-based Exit:** encerrar posição após X minutos se não evoluir (ex.: 30–45min).

---

## 5) Parâmetros Específicos por Estratégia

### 5.1) STP0003 — Larry Williams (Clássico)
- **Sinal:** rompimento com confirmação de direção por médias (`Rainbow_Charts_4`) / candle gatilho.
- **Filtro:** evitar operar contra `VWAP` e contra `HiLo` no timeframe mestre.
- **Janela:** 09:05–16:45.
- **Stop:** mínima/máxima da barra gatilho ou ATR.
- **Tamanho:** 1–3 contratos, ajustado por ATR.
- **Observações:** priorizar tendência já em formação.

```ntsl
if rainbow.up and close > vwap and breakout(high, period=3) then
  enter_long(size=calc_size(atr, risk));
  set_stop(min(low[-1], low[-2]));
  set_target_rr(2.0);
endif
```

---

### 5.2) V0061 — Stormer 901 (Alta Frequência)
- **Sinal:** micro-impulsos com `TTM_Squeeze` liberado + confirmação `Better_Volume`.
- **Filtro:** evitar spreads altos; `MaxTradesPerHour` = 6–10.
- **Janela:** 09:10–16:30 (evite abertura do leilão).
- **Stop:** técnico curto (última micro-estrutura) ou 0,7–1,0 × ATR curto.
- **Tamanho:** 1–2 contratos (scalp).
- **Observações:** desabilitar após 3 stops seguidos (cooldown 30 min).

```ntsl
if ttm.release and better_volume.trend_up and spread < max_spread then
  enter_long(size=scalp_size());
  set_stop(last_micro_low());
  set_target_points(8);  // ajuste WIN/WDO
  if consecutive_losses >= 3 then disable_for(30m); endif
endif
```

---

### 5.3) V0045 — Primeira Barra
- **Sinal:** rompimento da máxima/mínima da primeira barra do dia.
- **Filtro:** operar somente se `VWAP` alinhado e volume acima da média.
- **Janela:** 09:00–09:20 (somente).
- **Stop:** na extremidade oposta da primeira barra.
- **Tamanho:** 1–3 contratos.
- **Observações:** não reentrar se falhar duas vezes no mesmo dia.

```ntsl
if time in [09:00,09:20] and vwap_trend == up and high_break(first_bar.high) then
  enter_long(size=calc_size_firstbar());
  set_stop(first_bar.low);
  set_target_rr(1.5);
endif
```

---

### 5.4) BollingerBreakout — Rompimento de Bandas + Volume
- **Sinal:** fechamento fora da banda + confirmação `VFI` ou `WaveTrend`.
- **Filtro:** evitar logo nos primeiros 3 minutos de abertura; checar compressão prévia.
- **Janela:** 09:05–16:40.
- **Stop:** banda oposta ou `ATR*k`.
- **Tamanho:** 1–2 contratos.
- **Observações:** ideal pós-consolidação.

```ntsl
if close > bb.upper and vfi > 0 and was_consolidating(15) then
  enter_long(size=vol_size());
  set_stop(bb.middle or atr_stop());
  trail_by_atr(1.2);
endif
```

---

### 5.5) KASTR_SCALP_12R — Scalping Controlado
- **Sinal:** micro-impulso alinhado à `VWAP` + `SmartBar` (fluxo agressor).
- **Filtro:** spread estreito e latência baixa.
- **Janela:** 09:10–16:45.
- **Stop:** curtíssimo (micro-estrutura).
- **Tamanho:** 1–2 contratos; metas de 5–10 pts (WDO) ou 50–120 pts (WIN).
- **Observações:** limitar **MaxTradesPerHour** e aplicar cooldown após stop.

```ntsl
if price_above_vwap and smartbar.buy_pressure and spread < tick_threshold then
  enter_long(size=1);
  set_target_points(80);   // WIN exemplo
  set_stop(last_micro_low());
  cooldown_after_stop(5m);
endif
```

---

### 5.6) STP0006 — Setup 9.1 (Larry Williams)
- **Sinal:** padrão 9.1 pós-puxada, confirmação por `HiLo`/`SuperTrend`.
- **Filtro:** evitar contra `VWAP`.
- **Janela:** 09:15–16:30.
- **Stop:** mínima/máxima da barra de sinal ou ATR.
- **Tamanho:** 1–3 contratos.
- **Observações:** buscar 2R com parcial em 1R.

```ntsl
if setup_9_1 and supertrend.up and close > vwap then
  enter_long(size=calc_size(atr, risk));
  take_partial_at(1R);
  set_target_rr(2.0);
  move_to_breakeven_at(0.8R);
endif
```

---

## 6) Regras do Orquestrador (Pseudocódigo)

```ntsl
on_new_bar():
  signals = collect_signals()         // {strategy: {-1..+1}, confidence 0..1}
  scores  = weight_and_normalize(signals, profile_weights)
  if risk_engine.blocked(): return

  for asset in [WIN, WDO]:
    if session_filter.blocked(asset): continue

    score = scores[asset]
    if score >= THRESHOLD and not risk_engine.reached_limits(asset):
        // deduplicar: evitar múltiplas entradas idênticas
        if not orchestrator.position_exists(asset):
            size = risk_engine.calc_size(asset, atr(asset))
            place_order(asset, size, default_stops_targets(asset))
            log_signal(asset, score, signals)
```

**Conflitos:**  
- Se sinais contrários (compra vs venda) ocorrerem no mesmo ativo e timeframe:  
  - Priorizar **maior confiança × peso**.  
  - Se empate, **não operar** (ou reduzir size pela metade).

**Cooldowns Globais:**  
- Após 2 stops seguidos no mesmo ativo, pausar entradas novas por 20–30 min.

---

## 7) Ajustes Específicos — WIN vs WDO
- **WIN (Mini-Índice):** pontos maiores; metas comuns 80–200 pts (scalp) e 300–600 pts (tendência).  
- **WDO (Mini-Dólar):** metas 5–12 pts (scalp) e 15–25 pts (tendência).  
- **Slippage & Tick:** calibrar por ativo; usar tabelas distintas em `config.yaml`.

```yaml
# exemplo config por ativo
assets:
  WIN:
    tick: 5
    scalp_target_pts: [80, 120]
    trend_target_pts: [300, 600]
    slippage_pts: 10
  WDO:
    tick: 0.5
    scalp_target_pts: [6, 10]
    trend_target_pts: [15, 25]
    slippage_pts: 1.0
```

---

## 8) KPIs e Encerramento do Dia
- **KPIs mínimos para manter estratégia ativa:**  
  - Hit Ratio ≥ 45% (scalps) ou ≥ 35% (tendenciais), **PF ≥ 1.2**.  
- **Encerramento:**  
  - Encerrar todas as posições às 17:50.  
  - Se lucro ≥ `DailyGoal` (ex.: 2R), reduzir risco pela metade no restante do dia.  
  - Se MDD diária atingir `MaxDailyLoss`, **encerrar** o dia.

---

## 9) Backtest e Validação
- **Walk-forward** com janelas de 30–60 dias.  
- Testar perfis (Conservador/Moderado/Agressivo) separadamente.  
- Sensibilidade de parâmetros (ATR k, Threshold, pesos).  
- Exportar `metrics.json` e consolidar num dashboard.

---

## 10) Estrutura de Pastas (sugestão)
```
/automation
  /strategies
    stp0003_larry.ntsl
    v0061_stormer.ntsl
    v0045_primeirabarra.ntsl
    boll_breakout.ntsl
    kastr_scalp.ntsl
    stp0006_91.ntsl
  /orchestrator
    orchestrator.ntsl
    risk_engine.ntsl
    session_filter.ntsl
  /config
    config.yaml
    assets.yaml
    profiles.yaml
  /logs
    trades.log
    risk.log
    metrics.json
  /backtests
    results_YYYYMM.json
```

---

## 11) Checklist Operacional (Diário)
1. Verificar latência, feeds e relógio NTP.  
2. Carregar `profiles.yaml` (pesos do dia).  
3. Confirmar limites do `risk_engine`.  
4. Teste a **ordem simulada** (ping trade).  
5. Habilitar estratégias por janela (ex.: Primeira Barra).  
6. Acompanhar KPIs parciais (11:00 e 15:00).  
7. Encerramento forçado 17:50 + export de métricas.

---

### Nota Final
Este blueprint prioriza **consistência e proteção do capital**. Ajuste tamanhos/limiares ao seu perfil, valide em simulação e só então leve ao real.
