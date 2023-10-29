import random

exception_list = [StopIteration, ArithmeticError, FloatingPointError, OverflowError, ZeroDivisionError]
necessary_summ = 0
very_bad_num = 13

try:
    with open('out_file.txt', 'w') as out_file:
        while necessary_summ < 777:
            user_input = int(input("Введите число: "))
            necessary_summ += user_input
            out_file.write(str(user_input))
            out_file.write('\n')
            bad_num = random.choice([num for num in range(1, 14)])
            if bad_num == very_bad_num:
                raise random.choice(exception_list)

except (StopIteration, ArithmeticError, FloatingPointError, OverflowError, ZeroDivisionError):
    print('\nВас постигла неудача!')
finally:
    if necessary_summ >= 777:
        print('\nВы успешно выполнили условие для выхода из порочного цикла!')

    with open('out_file.txt', 'r') as out_file:
        current_summ = out_file.read()
        print('\nСодержимое файла out_file.txt:\n', current_summ)
