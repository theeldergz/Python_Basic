import functools
from typing import Callable, Optional

user_permissions = ['admin']


def check_permission(permission, _func: Optional[Callable] = None,) -> Callable:
    def decorator(func: Callable) -> Callable:
        """ Декоратор. Запускает декорируемую функцию только если права совпадают с admin """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if permission != 'admin':
                raise PermissionError('У пользователя недостаточно прав,'
                                f' чтобы выполнить функцию {func.__name__}')
            else:
                value = func(*args, **kwargs)
            return value

        return wrapper

    if _func is None:
        return decorator
    return decorator(_func)


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
