import os


def error_log_generator(path_to_log_file: str) -> None:
    """
    Функция принимает файл логов и создает отдельный файл с уровнем ERROR
    :param path_to_log_file: Пусть до файла с логом
    :return: None
    """
    with open(path_to_log_file, 'r', encoding='utf-8') as log_file:
        for line in log_file:
            if 'ERROR' in line:
                yield line


# При помощи модуля os (и функции join) сформируйте пути до файлов work_logs.txt и output.txt в папке data
# (output.txt может не быть в папке data, но его нужно будет там создать, при помощи кода)
input_file_path = os.path.join(r'C:\Users\Dionis\PycharmProjects'
                               r'\Python_Basic\Module26\05_logs_processing'
                               r'\data\work_logs.txt')

output_file_path = os.path.join(r'C:\Users\Dionis\PycharmProjects'
                                r'\Python_Basic\Module26\05_logs_processing'
                                r'\data\output.txt')
# Документация по join https://docs-python.ru/standart-library/modul-os-path-python/funktsija-join-modulja-os-path/

# Не забудьте проверить наличие файлов перед тем как начать работу с ними
# https://docs-python.ru/standart-library/modul-os-path-python/funktsija-exists-modulja-os-path/

with open(output_file_path, 'w') as output:
    for error_line in error_log_generator(input_file_path):
        output.write(error_line)
print("Файл успешно обработан.")