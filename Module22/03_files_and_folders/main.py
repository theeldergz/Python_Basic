import os


def dir_info(_path):
    count_files = 0
    size_files = 0
    count_directories = 0

    for file in os.listdir(_path):

        path_to_file = os.path.join(_path, file)

        if os.path.isdir(path_to_file):
            count_directories += 1
            summary_info = dir_info(path_to_file)

            size_files += summary_info[0]
            count_files += summary_info[1]
            count_directories += summary_info[2]
        else:
            if os.path.isfile(path_to_file):
                size_files += os.path.getsize(path_to_file)
                count_files += 1

    return size_files, count_files, count_directories


if __name__ == "__main__":
    size, file_count, dir_count = dir_info(r'C:\Users\Dionis\AppData\Local')

    print(
        'Размер каталога (в Кб): ', round((size / 1024), 2), 'КБ',
        '\nКоличество подкаталогов: ', dir_count,
        '\nКоличество файлов: ', file_count
    )
