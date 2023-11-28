from functools import wraps
from typing import Any, Callable


def cash_decor(func: Callable) -> Callable:
    """ Декоратор. Выдает закэшированное значение из словаря, если ключ уже известен """

    def wrapper(*args, **kwargs):
        if args[0] in wrapper.cash_dict.keys():
            return wrapper.cash_dict[args[0]]
        wrapper.cash_dict[args[0]] = func(*args, **kwargs)
        return wrapper.cash_dict[args[0]]

    wrapper.cash_dict = dict()
    return wrapper


@cash_decor
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


# Вычисление числа Фибоначчи с использованием кеширования
print(fibonacci(10))  # Результат будет кеширован

# Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша

# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и закеширован
