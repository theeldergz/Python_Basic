import functools
from typing import Callable


def counter(func: Callable) -> Callable:
    """ Декоратор. Считает количество вызовов декорируемой функции """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        wrapped_func.count += 1
        func(*args, **kwargs)
        print(f'Количество вызовов функции: {wrapped_func.count}')

    wrapped_func.count = 0
    return wrapped_func


@counter
def test_func() -> None:
    """ Функция формирует список из нечётных чисел от одного до N """

    num = 23
    odd_num: list = []

    for i in range(1, num + 1):
        if i % 2 != 0:
            odd_num.append(i)
    print(odd_num)


test_func()
test_func()
test_func()


