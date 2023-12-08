import functools
from typing import Callable, Optional

app = dict()


def callback(route_func: str, _func: Optional[Callable] = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        """ Декоратор передающий функцию в словарь по ключу route_func """
        app[route_func] = func

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    if _func is None:
        return decorator
    return decorator(_func)


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')

if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
