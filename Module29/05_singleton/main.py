import functools
from typing import Callable, Optional


def singleton(cls) -> Callable:
    """ Декоратор. Проверяет есть ли инстанс класса,
    если нет инстанса то создает его,
    в ином случае возвращает уже готовый инстанс"""
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if wrapper.instance:
            return wrapper.instance
        else:
            wrapper.instance = cls(*args, **kwargs)
            return wrapper.instance

    wrapper.instance = None
    return wrapper


@singleton
class Example:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


my_obj = Example('test')
my_another_obj = Example('test 2')

print(id(my_obj))
print(id(my_another_obj))
print(my_obj)
print(my_another_obj)
print(my_obj is my_another_obj)
