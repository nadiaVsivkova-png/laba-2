"""Модуль utils.

Содержит вспомогательные функции для валидации чисел и форматирования результатов.
"""

from typing import Any


def validate_number(value: Any) -> float:
    try:
        result = float(value)
        return result
    except (ValueError, TypeError):
        raise ValueError(f"Значение '{value}' не является числом")


def format_result(result: float, decimals: int = 2) -> str:
    return f'{result:.{decimals}f}'


def main() -> None:
    test_values = [5, 3.14, "10", "2.5", "abc", None]
    for val in test_values:
        try:
            result = validate_number(val)
            print(f"   validate_number({val}) = {result}")
        except ValueError as e:
            print(f"   validate_number({val}) -> Ошибка: {e}")

    test_cases = [
        (10.56789, 2),
        (5, 3),
        (3.14159, 1),
        (100.0, 0),
    ]

    for num, dec in test_cases:
        result = format_result(num, dec)
        print(f"format_result({num}, {dec}) = '{result}'")

if __name__ == "__main__":
    main()