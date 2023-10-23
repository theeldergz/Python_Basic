import os


user_input = input("Введите путь: ")
user_path = os.path.join(user_input)



def dir_info(user_path):

    count_files = 0
    size_files = 0
    count_directories = 0

    for file in os.listdir(user_path):

        path_to_file = os.path.join(user_path, file)

        if os.path.isdir(path_to_file):
            count_directories += 1
            size_files += dir_info(path_to_file)[0]
            count_files += dir_info(path_to_file)[1]
            count_directories += dir_info(path_to_file)[2]
        else:
            if os.path.isfile(path_to_file):
                size_files += os.path.getsize(path_to_file)
                count_files += 1

    return size_files, count_files, count_directories


size, file_count, dir_count = dir_info(user_path)

print(
    'Размер каталога (в Кб): ', round((size / 1024), 2), 'МБ',
    '\nКоличество подкаталогов: ', dir_count,
    '\nКоличество файлов: ', file_count
)
