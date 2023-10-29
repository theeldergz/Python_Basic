import math

def get_sage_sqrt(num):
    try:
        return math.sqrt(num)
    except ValueError as exc:
        print(f"\tЧисло {num} не может быть отрициательным или равным 0.\n\tТЕКСТ ОШИБКИ:", exc)
    except TypeError as exc:
        print(f"\tВведенный тип данных должен быть числом.\n\tВаш тип данных {type(num)}.\n\tТЕКСТ ОШИБКИ:", exc)
    except BaseException as exc:
        print("\tПроизошла непредвиденная ошибка: ", exc)

# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")