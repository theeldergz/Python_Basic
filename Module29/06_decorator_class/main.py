import functools
from typing import Callable, Optional
import time


class LoggerDecorator:
    """ Класс - декоратор. Логирует время работы функции, ее аргументы и результат выполнения """
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func
        self.start_time = time.time()

    def __call__(self, *args, **kwargs) -> Callable:
        print(f'Вызов функции {self.func.__name__}')
        print(f'Аргументы: {args}, {kwargs}')
        func_result = self.func(*args, **kwargs)
        print(f'Результат {func_result}')
        print('Время выполнения: {} секунды'.format(time.time() - self.start_time))
        return func_result


@LoggerDecorator
def complex_algorithm(arg1, arg2):
    # Здесь выполняется сложный алгоритм
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result


# Пример вызова функции с применением декоратора
result = complex_algorithm(10, 50)
