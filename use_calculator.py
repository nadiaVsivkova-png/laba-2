"""Скрипт для демонстрации использования пакета my_calculator.

Демонстрирует АБСОЛЮТНЫЙ импорт и работу с пакетом.
"""

from my_calculator import Calculator, validate_number, format_result


def main():
    calc = Calculator()
    # Демонстрация всех операций
    result = calc.add(15, 7)
    print(f"15 + 7 = {result}")

    result = calc.subtract(20, 9)
    print(f"20 - 9 = {result}")

    result = calc.multiply(8, 6)
    print(f"8 * 6 = {result}")

    result = calc.divide(100, 4)
    print(f"100 / 4 = {result}")

    # Демонстрация форматирования
    result = calc.divide(22, 7)
    for decimals in [0, 1, 2, 3, 4, 5]:
        formatted = format_result(result, decimals)
        print(f"  {decimals} знаков: {formatted}")

    # Демонстрация работы с разными типами данных
    print(f"  Числа: {calc.add(5, 3)}")

    print(f"  Строки: {calc.add('5', '3')}")

    print(f"  Смешанные: {calc.add(5, '3')}")

    # Демонстрация обработки ошибок
    try:
        calc.divide(10, 0)
    except ZeroDivisionError as e:
        print(f"  Деление на ноль: {e}")

    try:
        calc.add(5, "abc")
    except ValueError as e:
        print(f"  Неверные данные: {e}")

if __name__ == "__main__":
    main()