import functools
from typing import Any, Callable


def how_are_you(func: Callable) -> Any:
    """ Декоратор. Создает комическую ситуацию """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        print('Как дела? Хорошо?!')
        print('А у меня не очень! Ладно, держи свою функцию.')
        out_func = func(*args, **kwargs)
        return out_func

    return wrapped_func


@how_are_you
def test() -> list:
    num_list = list()
    for i in range(10):
        num_list.append(i)
    return num_list


print(test())
print(test.__name__)
