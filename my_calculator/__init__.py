"""Пакет my_calculator.

Предоставляет класс Calculator для арифметических операций
и вспомогательные функции для работы с числами.
"""

from .calculator import Calculator
from .utils import validate_number, format_result

__all__ = [
    "Calculator",
    "validate_number",
    "format_result",
]

__version__ = "0.1.0"
