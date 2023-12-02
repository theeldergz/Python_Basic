import os


class NewOpen:

    """
    Класс являющийся контекстным менеджером открытия файлов.
    Отличается тем, что если файл не найден он будет создан
    """

    def __init__(self, file_name: str, open_mode: str, encoding='utf-8') -> None:
        """
        :param file_name: отвечает за имя файла
        :param open_mode: отвечает за режим открытия файла
        :param encoding: отвечает за кодировку файла
        """
        self.file_name = file_name
        self.open_mode = open_mode
        self.encoding = encoding
        self.file_path = os.path.abspath(self.file_name)

    def __enter__(self) -> 'NewOpen':
        """
        Метод отвечает за проверку и открытие файла. Если файл не найден, здесь же создается нужный файл
        :return: self?
        """
        if os.path.exists(self.file_path):
            print('gfg')
            self.open_file = open(self.file_name, self.open_mode, encoding=self.encoding)
        else:
            self.open_file = open(self.file_name, 'a+', encoding=self.encoding)

        return self

    def write(self, line: str) -> None:
        """
        Тестовый метод write для данного контекстного менеджера, просто дублирует write
        :param line: обьект типа str который необходимо записить в файл
        :return: None
        """
        self.open_file.write(line)

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.open_file.close()
        return True


with NewOpen('test_file', 'w') as test_file:
    test_file.write('test')
