class LRUCache:
    def __init__(self, capacity: int) -> None:
        """
        Создает пустой список для хранения добавляемых элементов
        :param capacity: Максимальный размер спика (кол-во элементов в кеше)
        """

        self.cache_list = list()
        self.capacity: int = capacity

    def print_cache(self) -> None:
        """ Выводит текущий кеш список в консоль """

        print('\nLRU Cache:')
        for item in self.cache_list:
            print(item[0], ': ', item[1])

    @property
    def cache(self) -> tuple:
        """ Возвращет самый старый элемент """

        return self.cache_list[-1]

    @cache.setter
    def cache(self, item: tuple[str, str]) -> None:
        """
        Добавляет новый элемент
        :param item: кортеж из двух строка вида ключ: значение
        :return: None
        """

        key, value = item[0], item[1]
        if len(self.cache_list) < self.capacity:
            self.cache_list.insert(0, (key, value))
        else:
            self.cache_list.pop()
            self.cache_list.insert(0, (key, value))

    def get(self, key: str) -> str:
        """
        Возвращает значение по ключу key, поднимает приоритет по этому запросу
        :param key: Ключ по которому необходимо вернуть значение
        :return: Строку - значение по ключу key
        """

        pop_index = None
        return_elem = None
        for index, item in enumerate(self.cache_list):
            if key == item[0]:
                pop_index = index
                return_elem = item[0]
        pop_elem = self.cache_list.pop(pop_index)
        self.cache_list.insert(0, pop_elem)
        return return_elem



# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print('\nGET: ')
print(cache.get("key2"))  # value2
print(cache.get("key3"))
# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4