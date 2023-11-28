from datetime import datetime
import functools
import time
from typing import Callable


def go_slow(func: Callable) -> Callable:
    """ Декоратор. Заставляет функцию работать медленнее """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        current_time = datetime.now().strftime("%H:%M:%S")
        print('Время запуска декоратора: ', current_time)
        time.sleep(5)
        func(*args, **kwargs)
        return func

    return wrapped_func


@go_slow
def test_func():
    """ Выводит текущее время """

    current_time = datetime.now().strftime("%H:%M:%S")
    print('Время запуска функции: ', current_time)


test_func()

