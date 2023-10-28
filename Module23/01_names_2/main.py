summ_symbols = 0
strings_with_err = []
try:
    with open('people.txt', encoding='utf-8') as peopletxt:
        for index, line in enumerate(peopletxt, start=1):
            if line.endswith('\n'):
                if (len(line) - 1) < 3:
                    strings_with_err.append(index)
                    raise ValueError
            else:
                if len(line) < 3:
                    strings_with_err.append(index)
                    raise ValueError
except FileNotFoundError:
    print('файл или директория не существует')
except ValueError:
    with open('errors.log', 'a') as logs:
        logs.write('\nОшибка: менее трёх символов в строке(ах): {}'.format(*strings_with_err))
    print(('Ошибка: менее трёх символов в строке(ах): {}'.format(*strings_with_err)))
finally:
    with open('people.txt', encoding='utf-8') as peopletxt:
        for index, line in enumerate(peopletxt, start=1):
            if line.endswith('\n'):
                summ_symbols -= 1
                if len(line) < 3:
                    print(len(line))
            summ_symbols += len(line)
    print('Общее количество символов: {}'.format(summ_symbols))

