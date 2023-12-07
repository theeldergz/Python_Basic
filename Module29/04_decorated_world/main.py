import functools
from typing import Callable, Optional


def decorator_with_args_for_any_decorator(_decorator: Callable) -> Callable:
    """ Декоратор, даёт возможность любому декоратору принимать произвольные аргументы. """
    @functools.wraps(_decorator)
    def inner_decorator(*args, **kwargs):
        def wrapper_decorator(func):
            return _decorator(func, *args, **kwargs)
        return wrapper_decorator
    return inner_decorator


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *_args, **_kwargs) -> Callable:
    """ Декоратор. Показывает какие *args и **kwargs были переданы в этот же декоратор """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Переданные арги и кварги в декоратор: {args}, {kwargs}')
        return func(*args, **kwargs)
    return wrapper

@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
