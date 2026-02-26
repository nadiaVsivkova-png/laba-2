"""Модуль calculator.

Содержит класс Calculator для выполнения основных арифметических операций.
"""

from .utils import validate_number, format_result

class Calculator:

    def add(self, a: float, b: float) -> float:
        a = validate_number(a)
        b = validate_number(b)
        return a + b

    def subtract(self, a: float, b: float) -> float:
        a = validate_number(a)
        b = validate_number(b)
        return a - b

    def multiply(self, a: float, b: float) -> float:
        a = validate_number(a)
        b = validate_number(b)
        return a * b

    def divide(self, a: float, b: float) -> float:
        a = validate_number(a)
        b = validate_number(b)

        if b == 0:
            raise ZeroDivisionError("Деление на ноль запрещено")

        return a / b


def main() -> None:
    calc = Calculator()
    print(f"10 + 5 = {calc.add(10, 5)}")

    print(f"20 - 8 = {calc.subtract(20, 8)}")

    print(f"7 * 6 = {calc.multiply(7, 6)}")

    print(f"45 / 9 = {calc.divide(45, 9)}")

    print(f"'10' + '5' = {calc.add("10", "5")}")

    try:
        print(f"10 / 0 = {calc.divide(10, 0)}")
    except ZeroDivisionError as e:
        print(f"Ошибка при делении на ноль: {e}")

    try:
        print(f"5 + 'abc' = {calc.add(5, "abc")}")
    except ValueError as e:
        print(f"Ошибка при неверных данных: {e}")

    print(f"10 / 3 = {calc.divide(10, 3)}")
    print(f"10 / 3 = {format_result(calc.divide(10, 3), 4)} (с 4 знаками)")

if __name__ == "__main__":
    main()