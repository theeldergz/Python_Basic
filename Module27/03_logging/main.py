from datetime import datetime
import functools
from typing import Any, Callable


def logging(func: Callable) -> Any:
    """ Декоратор. Логирует работу функции, собирает информацию об ошибках в function_errors.log"""

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except (TypeError, ValueError) as exc:
            with open('function_errors.log', 'a', encoding='utf-8') as logs:
                logs.write('\n_ERROR --> {err_name}, произошла в {time}'.format(err_name=exc, time=datetime.now()))
    return wrapped_func


@logging
def test_logs() -> None:
    """ Умножает число на 2) """
    user_input = int(input('Введите число которое необходимо умножить на 2! '))
    user_input *= 2
    print(user_input)

test_logs()

