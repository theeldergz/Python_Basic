import os

test_path = r'C:\Users\Dionis\PycharmProjects\Python_Basic\Module17'


def str_count(user_path):
    str_counter = 0

    for direct in os.listdir(user_path):
        temp_path = os.path.join(user_path, direct)
        if os.path.isfile(temp_path):
            if temp_path.endswith('.py'):

                with open(temp_path, 'r', encoding='utf-8') as python_file:
                    for line in python_file:
                        if not line.startswith('#') and line != '\n':
                            str_counter += 1
                yield str_counter
                str_counter = 0
        else:
            for file in str_count(temp_path):
                str_counter += file
                yield str_counter
                str_counter = 0


test = str_count(test_path)
for count_sym in test:
    print('Количество строк: ', count_sym)
