{===============================
 ESTUDO VISUAL - DAY TRADE PRO (NTSL / PROFIT)
 - Versão: 3.5 Pro (Estrutura Final)
===============================}

Input
  // -------- MODO DEBUG --------
  modoDebug(False); // Ative para colorir as barras e ver qual filtro está bloqueando os sinais

  // -------- ESTRATÉGIA --------
  estrategia("CONFLUENCE"); // CASH, VWAP ou CONFLUENCE

  // -------- CASH BANDS --------
  emaCurta(9);
  emaLonga(21);
  atrLen(14);
  fatorBandaATR(1.2);
  maxDistMedias(300.0);
  
  // -------- VWAP BANDS --------
  vwapDesvioPct(0.25);
  
  // -------- CONFLUÊNCIA --------
  minConfluencias(2);
  
  // -------- FILTROS --------
  filtroVolumeAtivado(True);
  volumeMinimo(1.5);
  volumePeriodos(20);
  duoAtrLen(24);
  spikeATRmult(2.0);
  spikeBloqueioBars(5);
  maxSpreadPontos(3.0);

  // -------- VISUAL --------
  plotarBandasCash(True);
  plotarBandasVWAP(True);
  plotarSinaisCompra(True);
  plotarSinaisVenda(True);

Var
  // Variáveis de Plotagem e Estado
  sinalEC, sinalEL, atrCash, sinalBandaSup, sinalBandaInf: Float;
  sinalV, desvioVwap, vwapBandaSup, vwapBandaInf: Float;
  spikeBlockCount: Integer;
  
  // Variáveis de Lógica
  sinal, cashSinal, vwapSinal, rsiSinal, confluenciaSinal: Integer;
  podeEntrar: Boolean;
  atrSpike, baseAtrSpike: Float;
  filtroVolOk, filtroSpreadOk: Boolean;

// ======== FUNÇÕES ========

function FiltroVolume(pAtivado: Boolean; pPeriodos: Integer; pVolMin: Float): Boolean;
var volMedio: Float;
begin
  if (not pAtivado) then Result := True
  else
  begin
    volMedio := Media(pPeriodos, Volume);
    if (volMedio > 0) then Result := Volume >= (volMedio * pVolMin)
    else Result := True;
  end;
end;

function FiltroSpread(pMaxSpread: Float): Boolean;
var spread: Float;
begin
  spread := AskPrice - BidPrice;
  Result := spread <= pMaxSpread;
end;

function SinalCash(pEC, pEL, pBandaSup, pBandaInf: Float): Integer;
begin
  if (pEC > pEL) and (Low <= pBandaInf) and (Close > pBandaInf) then Result := 1
  else if (pEC < pEL) and (High >= pBandaSup) and (Close < pBandaSup) then Result := -1
  else Result := 0;
end;

function SinalVWAP(pVwapBandaSup, pVwapBandaInf: Float): Integer;
begin
  if (Close < pVwapBandaInf) and (Close > Low) then Result := 1
  else if (Close > pVwapBandaSup) and (Close < High) then Result := -1
  else Result := 0;
end;

function SinalRSI: Integer;
var valRSI: Float;
begin
  valRSI := RSI(14, 0);
  if (valRSI < 30) and (valRSI > valRSI[1]) then Result := 1
  else if (valRSI > 70) and (valRSI < valRSI[1]) then Result := -1
  else Result := 0;
end;

function GeraConfluencia(pMinConfluencias: Integer; pCashSinal, pVwapSinal, pRsiSinal: Integer): Integer;
var confluencias: Integer;
begin
  confluencias := 0;
  if (pCashSinal = 1) then confluencias := confluencias + 1;
  if (pVwapSinal = 1) then confluencias := confluencias + 1;
  if (pRsiSinal = 1) then confluencias := confluencias + 1;
  if (confluencias >= pMinConfluencias) then Result := 1
  else
  begin
    confluencias := 0;
    if (pCashSinal = -1) then confluencias := confluencias + 1;
    if (pVwapSinal = -1) then confluencias := confluencias + 1;
    if (pRsiSinal = -1) then confluencias := confluencias + 1;
    if (confluencias >= pMinConfluencias) then Result := -1
    else Result := 0;
  end;
end;

// ======== BLOCO PRINCIPAL DE EXECUÇÃO ========
begin
  // --- Lógica de Spike ---
  atrSpike := AvgTrueRange(atrLen, 2);
  baseAtrSpike := AvgTrueRange(duoAtrLen, 2);
  if (baseAtrSpike > 0) and (atrSpike >= spikeATRmult * baseAtrSpike) then spikeBlockCount := spikeBloqueioBars
  else if (spikeBlockCount > 0) then spikeBlockCount := spikeBlockCount - 1;

  // --- CÁLCULO DOS INDICADORES ---
  sinalEC := MediaExp(emaCurta, Close);
  sinalEL := MediaExp(emaLonga, Close);
  atrCash := AvgTrueRange(atrLen, 2);
  sinalBandaSup := sinalEL + fatorBandaATR * atrCash;
  sinalBandaInf := sinalEL - fatorBandaATR * atrCash;

  sinalV := VWAP(1);
  desvioVwap := sinalV * (vwapDesvioPct / 100.0);
  vwapBandaSup := sinalV + desvioVwap;
  vwapBandaInf := sinalV - desvioVwap;

  // --- OBTENÇÃO DOS SINAIS ---
  if Abs(sinalEC - sinalEL) >= maxDistMedias then cashSinal := 0
  else cashSinal := SinalCash(sinalEC, sinalEL, sinalBandaSup, sinalBandaInf);
  
  vwapSinal := SinalVWAP(vwapBandaSup, vwapBandaInf);
  rsiSinal := SinalRSI();
  confluenciaSinal := GeraConfluencia(minConfluencias, cashSinal, vwapSinal, rsiSinal);

  // --- Lógica de Sinais e Filtros ---
  if (estrategia = "CASH") then sinal := cashSinal
  else if (estrategia = "VWAP") then sinal := vwapSinal
  else if (estrategia = "CONFLUENCE") then sinal := confluenciaSinal
  else sinal := 0;

  filtroVolOk := FiltroVolume(filtroVolumeAtivado, volumePeriodos, volumeMinimo);
  filtroSpreadOk := FiltroSpread(maxSpreadPontos);
  podeEntrar := (spikeBlockCount = 0) and filtroVolOk and filtroSpreadOk;

  // --- LÓGICA DE PLOTAGEM (NORMAL OU DEBUG) ---
  if (modoDebug) then
  begin
    if (spikeBlockCount > 0) then PaintBar(clRed) // Vermelho = Bloqueado por Spike
    else if (not filtroVolOk) then PaintBar(clBlue) // Azul = Bloqueado por Volume Baixo
    else if (not filtroSpreadOk) then PaintBar(clYellow); // Amarelo = Bloqueado por Spread Alto
  end
  else
  begin
    // Plotagem de Sinais
    if (podeEntrar) then
    begin
      if (sinal = 1) and (plotarSinaisCompra) then PlotText("C", clGreen, 0, 10, Low)
      else if (sinal = -1) and (plotarSinaisVenda) then PlotText("V", clRed, 0, 10, High);
    end;
    
    // Plotagem das Linhas
    if (plotarBandasCash) then
    begin
      Plot(sinalBandaSup);
      SetPlotColor(1, clRed);
      Plot2(sinalBandaInf);
      SetPlotColor(2, clGreen);
      Plot3(sinalEL);
      SetPlotColor(3, clYellow);
      Plot4(sinalEC);
      SetPlotColor(4, clBlue);
    end;

    if (plotarBandasVWAP) then
    begin
      Plot5(vwapBandaSup);
      SetPlotColor(5, clRed);
      SetPlotStyle(5, 2);
      Plot6(vwapBandaInf);
      SetPlotColor(6, clGreen);
      SetPlotStyle(6, 2);
      Plot7(sinalV);
      SetPlotColor(7, clFuchsia);
      SetPlotWidth(7, 2);
    end;
  end;

  // Plot invisível para forçar a plotagem na janela do preço
  Plot99(Close, "", clNone);

end;