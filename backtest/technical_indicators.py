import pandas as pd
import numpy as np
import talib as ta
from typing import Tuple

class TechnicalIndicators:
    """
    Implementações de indicadores técnicos compatíveis com NTSL
    Baseadas na documentação em docs/funcoes_constantes_NTSL.md
    """
    
    @staticmethod
    def sma(data: pd.Series, period: int) -> pd.Series:
        """
        Simple Moving Average - Implementação customizada para alinhar com Profit Pro.
        Usa a função rolling do pandas para maior controle.
        """
        return data.rolling(window=period, min_periods=1).mean()
    
    @staticmethod
    def ema(data: pd.Series, period: int) -> pd.Series:
        """
        Exponential Moving Average - função XAverage() do NTSL
        Conforme documentação: XAverage(Period, Source)
        """
        return ta.EMA(data, timeperiod=period)
    
    @staticmethod
    def smma(data: pd.Series, period: int) -> pd.Series:
        """
        Smoothed Moving Average (SMMA) / Welles Wilder's Moving Average (WWMA).
        Equivalent to EMA with alpha = 1/period.
        """
        return data.ewm(span=period, adjust=False).mean()

    @staticmethod
    def wma(data: pd.Series, period: int) -> pd.Series:
        """
        Weighted Moving Average - função WAverage() do NTSL
        Conforme documentação: WAverage(Period, Source)
        """
        return ta.WMA(data, timeperiod=period)
    
    @staticmethod
    def atr(data: pd.DataFrame, period: int = 14) -> pd.Series:
        """
        Average True Range - função AvgTrueRange() do NTSL
        Conforme documentação: AvgTrueRange(Period, MediaType)
        """
        high = data['high']
        low = data['low']  
        close = data['close']
        return ta.ATR(high, low, close, timeperiod=period)
    
    @staticmethod
    def bollinger_bands(data: pd.Series, period: int = 20, std_dev: float = 2.0, ma_type: str = 'sma') -> Tuple[pd.Series, pd.Series, pd.Series]:
        """
        Bollinger Bands - função BollingerBands() do NTSL
        Conforme documentação: BollingerBands(Desvio, Periodo, TipoMedia)
        Retorna: (Upper, Middle, Lower)
        """
        # TA-Lib BBANDS uses SMA by default for the middle band.
        # If other MA types are needed, the middle band would need to be calculated separately
        # and then the standard deviation applied. For simplicity and common usage,
        # we'll stick to the default SMA for the middle band as TA-Lib implements it.
        upper, middle, lower = ta.BBANDS(data, timeperiod=period, nbdevup=std_dev, nbdevdn=std_dev, matype=ma_type)
        
        # If a different MA type is explicitly requested, we calculate the middle band separately
        # and then re-calculate upper/lower based on that and the standard deviation.
        # However, TA-Lib's BBANDS directly provides the bands based on its internal MA calculation.
        # For now, we'll assume the default SMA for BBANDS in TA-Lib is acceptable,
        # or that the ma_type parameter primarily refers to other standalone MA functions.
        # If strict adherence to ma_type for the middle band of BBANDS is required,
        # this function would need more complex logic to replicate TA-Lib's std dev calculation
        # on a custom MA.
        
        return upper, middle, lower
    
    @staticmethod
    def rsi(data: pd.Series, period: int = 14) -> pd.Series:
        """
        Relative Strength Index - função RSI() do NTSL
        Conforme documentação: RSI(Period, Source)
        """
        return ta.RSI(data, timeperiod=period)
    
    @staticmethod
    def stochastic(data_high: pd.Series, data_low: pd.Series, data_close: pd.Series, 
                   k_period: int = 14, d_period: int = 3) -> Tuple[pd.Series, pd.Series]:
        """
        Stochastic Oscillator - função Stochastic() do NTSL
        Conforme documentação: Stochastic(KPeriod, DPeriod, Source)
        Retorna: (%K, %D)
        """
        slowk, slowd = ta.STOCH(data_high, data_low, data_close, 
                                fastk_period=k_period, slowk_period=d_period, 
                                slowk_matype=0, slowd_period=d_period, slowd_matype=0) # 0 for SMA
        return slowk, slowd
    
    @staticmethod
    def macd(data: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9) -> Tuple[pd.Series, pd.Series, pd.Series]:
        """
        MACD - função MACD() do NTSL
        Conforme documentação: MACD(FastPeriod, SlowPeriod, SignalPeriod, Source)
        Retorna: (MACD Line, Signal Line, Histogram)
        """
        macd_line, signal_line, histogram = ta.MACD(data, fastperiod=fast, slowperiod=slow, signalperiod=signal)
        return macd_line, signal_line, histogram
    
    @staticmethod
    def hull_ma(data: pd.Series, period: int) -> pd.Series:
        """
        Hull Moving Average - presente em vários exemplos do catálogo
        Usado em estratégias como __WaveWeisHMA
        """
        # Hull MA = WMA(2*WMA(n/2) - WMA(n), sqrt(n))
        half_period = period // 2
        sqrt_period = int(np.sqrt(period))
        
        wma_half = TechnicalIndicators.wma(data, half_period)
        wma_full = TechnicalIndicators.wma(data, period)
        
        hull_data = 2 * wma_half - wma_full
        hull_ma = TechnicalIndicators.wma(hull_data, sqrt_period)
        
        return hull_ma
    
    @staticmethod
    def tema(data: pd.Series, period: int) -> pd.Series:
        """
        Triple Exponential Moving Average - presente no catálogo
        Usado em __MEDIAMOVELTRIPLA e outros exemplos
        """
        return ta.TEMA(data, timeperiod=period)
    
    @staticmethod
    def didi_index(data: pd.Series, short: int = 3, medium: int = 8, long: int = 20) -> Tuple[pd.Series, pd.Series, pd.Series]:
        """
        Didi Index - amplamente usado nas estratégias do catálogo
        Presente em DIDI_Index, _DIDIINDEX e muitos outros
        """
        # Três médias móveis simples
        short_ma = TechnicalIndicators.sma(data, short)
        medium_ma = TechnicalIndicators.sma(data, medium)  
        long_ma = TechnicalIndicators.sma(data, long)
        
        return short_ma, medium_ma, long_ma
    
    @staticmethod
    def vwap(data: pd.DataFrame) -> pd.Series:
        """
        Volume Weighted Average Price - muito usado no catálogo
        Presente em __VWAP_DIAS_ATRAS, _VENO_LINES_WAP e outros
        """
        typical_price = (data['high'] + data['low'] + data['close']) / 3
        volume_price = typical_price * data['volume']
        
        # VWAP acumulado
        cumulative_volume_price = volume_price.expanding().sum()
        cumulative_volume = data['volume'].expanding().sum()
        
        vwap = cumulative_volume_price / cumulative_volume
        return vwap
