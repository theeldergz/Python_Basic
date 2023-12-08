import time
import functools
from typing import Callable


def logged(func: Callable, time_format: str, cls) -> Callable:
    """
    Декоратор. Логирует время запуска и время работы метода
    :param func: метод класса который декорируется
    :param time_format: формат отображения времени для метода strftime модуля time
    :param cls: класс метода
    """

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        start_time = time.time()
        formatted_date = time.strftime(time_format, time.localtime())
        print(f'Запускается {cls.__name__}.{func.__name__}. Дата и время запуска: {formatted_date}')
        value = func(*args, **kwargs)
        stop_time = round(time.time() - start_time, 3)
        print(f'Завершение {cls.__name__}.{func.__name__}, время работы = {stop_time}s')
        return value

    return wrapped


def log_methods(time_format: str) -> Callable:
    """
    Декоратор. Оборачивает методы класса в декоратор logged
    :param time_format: Формат отображение даты
    """

    def class_decorator(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                method = getattr(cls, i_method_name)
                decor_method = logged(method, time_format, cls)
                setattr(cls, i_method_name, decor_method)
        return cls

    return class_decorator


@log_methods("%b %d %Y - %H:%M:%S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("%b %d %Y - %H:%M:%S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1 от класса A в классе B(A)")

    def test_sum_2(self):
        print("Метод test sum 2 у B(A)")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
