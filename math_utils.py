"""Модуль math_utils.

Содержит функции для работы с числами:
- Проверка на простоту
- Вычисление факториала
- Вычисление чисел Фибоначчи
"""


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел")

    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Номер числа Фибоначчи не может быть отрицательным")

    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1  # a = F(0), b = F(1)
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def main() -> None:
    print('Проверка простых чисел (is_prime):')
    print(f' is_prime(7) = {is_prime(7)}')
    print(f' is_prime(7) = {is_prime(10)}')
    print(f' is_prime(7) = {is_prime(2)}')
    print(f' is_prime(7) = {is_prime(1)}')


    print('\nВычисление факториала (factorial):')
    print(f'factorial(0) = {factorial(0)}')
    print(f'factorial(0) = {factorial(1)}')
    print(f'factorial(0) = {factorial(5)}')
    print(f'factorial(0) = {factorial(10)}')


    print('\nЧисла Фибоначчи (fibonacci):')
    print(f'factorial(0) = {factorial(0)}')
    print(f'factorial(0) = {factorial(1)}')
    print(f'factorial(0) = {factorial(5)}')
    print(f'factorial(0) = {factorial(10)}')
if __name__ == "__main__":
    main()
