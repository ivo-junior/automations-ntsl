import pandas as pd
import numpy as np
from typing import Tuple

class TechnicalIndicators:
    """
    Implementações de indicadores técnicos compatíveis com NTSL
    Baseadas na documentação em docs/funcoes_constantes_NTSL.md
    """
    
    @staticmethod
    def sma(data: pd.Series, period: int) -> pd.Series:
        """
        Simple Moving Average - função Media() do NTSL
        Conforme documentação: Media(Period, Source)
        """
        return data.rolling(window=period, min_periods=1).mean()
    
    @staticmethod
    def ema(data: pd.Series, period: int) -> pd.Series:
        """
        Exponential Moving Average - função XAverage() do NTSL
        Conforme documentação: XAverage(Period, Source)
        """
        return data.ewm(span=period, adjust=False).mean()
    
    @staticmethod
    def wma(data: pd.Series, period: int) -> pd.Series:
        """
        Weighted Moving Average - função WAverage() do NTSL
        Conforme documentação: WAverage(Period, Source)
        """
        weights = np.arange(1, period + 1)
        return data.rolling(window=period, min_periods=1).apply(
            lambda x: np.average(x, weights=weights[:len(x)]), raw=True
        )
    
    @staticmethod
    def atr(data: pd.DataFrame, period: int = 14) -> pd.Series:
        """
        Average True Range - função AvgTrueRange() do NTSL
        Conforme documentação: AvgTrueRange(Period, MediaType)
        """
        high = data['high']
        low = data['low']  
        close = data['close']
        
        # True Range calculation
        tr1 = high - low
        tr2 = abs(high - close.shift(1))
        tr3 = abs(low - close.shift(1))
        
        true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        
        # ATR é a média móvel exponencial do True Range para maior reatividade
        return true_range.ewm(span=period, adjust=False).mean()
    
    @staticmethod
    def bollinger_bands(data: pd.Series, period: int = 20, std_dev: float = 2.0, ma_type: str = 'sma') -> Tuple[pd.Series, pd.Series, pd.Series]:
        """
        Bollinger Bands - função BollingerBands() do NTSL
        Conforme documentação: BollingerBands(Desvio, Periodo, TipoMedia)
        Retorna: (Upper, Middle, Lower)
        """
        # Selecionar o tipo de média com base no parâmetro
        if ma_type.lower() == 'ema':
            middle = TechnicalIndicators.ema(data, period)
        elif ma_type.lower() == 'wma':
            middle = TechnicalIndicators.wma(data, period)
        else: # Padrão é SMA
            middle = TechnicalIndicators.sma(data, period)
        
        # Desvio padrão
        std = data.rolling(window=period, min_periods=1).std()
        
        # Bandas superior e inferior
        upper = middle + (std * std_dev)
        lower = middle - (std * std_dev)
        
        return upper, middle, lower
    
    @staticmethod
    def rsi(data: pd.Series, period: int = 14) -> pd.Series:
        """
        Relative Strength Index - função RSI() do NTSL
        Conforme documentação: RSI(Period, Source)
        """
        delta = data.diff()
        
        # Separar ganhos e perdas
        gains = delta.where(delta > 0, 0)
        losses = -delta.where(delta < 0, 0)
        
        # Calcular médias móveis (Wilder's smoothing)
        avg_gains = gains.ewm(alpha=1/period, adjust=False).mean()
        avg_losses = losses.ewm(alpha=1/period, adjust=False).mean()
        
        # RSI calculation
        rs = avg_gains / avg_losses
        rsi = 100 - (100 / (1 + rs))
        
        return rsi
    
    @staticmethod
    def stochastic(data_high: pd.Series, data_low: pd.Series, data_close: pd.Series, 
                   k_period: int = 14, d_period: int = 3) -> Tuple[pd.Series, pd.Series]:
        """
        Stochastic Oscillator - função Stochastic() do NTSL
        Conforme documentação: Stochastic(KPeriod, DPeriod, Source)
        Retorna: (%K, %D)
        """
        # Encontrar a mínima mais baixa e máxima mais alta no período
        lowest_low = data_low.rolling(window=k_period, min_periods=1).min()
        highest_high = data_high.rolling(window=k_period, min_periods=1).max()
        
        # Calcular %K
        k_percent = 100 * ((data_close - lowest_low) / (highest_high - lowest_low))
        
        # Calcular %D (média móvel simples de %K)
        d_percent = k_percent.rolling(window=d_period, min_periods=1).mean()
        
        return k_percent, d_percent
    
    @staticmethod
    def macd(data: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9) -> Tuple[pd.Series, pd.Series, pd.Series]:
        """
        MACD - função MACD() do NTSL
        Conforme documentação: MACD(FastPeriod, SlowPeriod, SignalPeriod, Source)
        Retorna: (MACD Line, Signal Line, Histogram)
        """
        # EMAs rápida e lenta
        ema_fast = data.ewm(span=fast, adjust=False).mean()
        ema_slow = data.ewm(span=slow, adjust=False).mean()
        
        # Linha MACD
        macd_line = ema_fast - ema_slow
        
        # Linha de sinal
        signal_line = macd_line.ewm(span=signal, adjust=False).mean()
        
        # Histograma
        histogram = macd_line - signal_line
        
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
        # TEMA = 3*EMA - 3*EMA(EMA) + EMA(EMA(EMA))
        ema1 = data.ewm(span=period, adjust=False).mean()
        ema2 = ema1.ewm(span=period, adjust=False).mean()
        ema3 = ema2.ewm(span=period, adjust=False).mean()
        
        tema = 3 * ema1 - 3 * ema2 + ema3
        return tema
    
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
