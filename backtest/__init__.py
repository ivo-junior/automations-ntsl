"""
Sistema de Backtest para Estratégias NTSL
=========================================

Este módulo permite testar estratégias NTSL contra dados históricos
para análise de performance e otimização de parâmetros.
"""

__version__ = "1.0.0"
__author__ = "Trader-Dev NTSL"

from .ntsl_parser import NTSLParser
from .backtest_engine import BacktestEngine
from .data_provider import DataProvider

__all__ = [
    'NTSLParser',
    'BacktestEngine', 
    'DataProvider'
]
