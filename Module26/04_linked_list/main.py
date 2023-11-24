class LinkedList:
    def __init__(self):
        self.__id = 0
        self.__global_elem_counter = 0
        self.__separate_sym = '$'
        self.__prefix_id = 'id='
        self.__str_of_num = ''
        self.__elem_counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        while self.__elem_counter < self.__id:
            self.__elem_counter += 1
            __required_string = self.__prefix_id + str(self.__elem_counter)
            if __required_string in self.__str_of_num:
                return self.get(self.__elem_counter)
        raise StopIteration

    def __str__(self):
        __line_out = ''
        for __index in range(self.__id):
            __required_string = self.__prefix_id + str(__index)
            if __required_string in self.__str_of_num:
                __line_out += self.get(__index) + ' '
        return f'[{__line_out}]'

    def append(self, number: int):
        self.__str_of_num += self.__prefix_id + str(self.__id) + str(number) + self.__separate_sym
        self.__id += 1
        self.__global_elem_counter += 1

    def __elem_finder(self, __index):
        __required_string = self.__prefix_id + str(__index)  # создает пример нужного префикса строки
        __length_prefix = len(__required_string)  # измеряет длину префикс
        __left_length = self.__str_of_num.find(__required_string) + __length_prefix  # индекс старта среза
        __right_length = self.__str_of_num.index(self.__separate_sym, __left_length)  # индекс конца среза
        return __left_length, __right_length

    def get(self, __index):
        __start_get, __end_get = self.__elem_finder(__index)

        return self.__str_of_num[__start_get:__end_get]

    def remove(self, __index):
        __prefix_len = len(self.__prefix_id + str(__index))
        __start_get, __end_get = self.__elem_finder(__index)
        __start_get -= __prefix_len
        self.__str_of_num = self.__str_of_num[:__start_get] + self.__str_of_num[__end_get + 1:]
        self.__global_elem_counter -= 1


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)

for elem in my_list:
    print('Первый элемент: ', elem)
