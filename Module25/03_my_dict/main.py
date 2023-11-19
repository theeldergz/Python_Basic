class MyDict:
    def __init__(self):
        self.__key_list = list()
        self.__value_list = list()

    def __str__(self):
        __line = []
        for i, _ in enumerate(self.__key_list):
            __line.append(str(self.__key_list[i]) + ': ' + str(self.__value_list[i]))
        line = " ".join(__line)

        return '{' + line + '}'

    def update(self, external_key, external_value):
        if not isinstance(external_key, (tuple, frozenset, str, int, float, bool)):
            raise TypeError
        else:
            if external_key not in self.__key_list:
                self.__key_list.append(external_key)
                self.__value_list.append(external_value)
            else:
                index = self.__key_list.index(external_key)
                self.__value_list[index] = external_value

    def get(self, external_key, external_value=None):
        if not isinstance(external_key, (tuple, frozenset, str, int, float, bool)):
            raise TypeError
        else:
            if external_key not in self.__key_list:
                return 0
            else:
                self.__key_list.append(external_key)
                index = self.__key_list.index(external_key)
                return self.__value_list[index]


dict_test = MyDict()
print(dict_test)
dict_test.update('String1', 10)
print(dict_test)
dict_test.update('String2', 14)
dict_test.update('String3', 1235)
print(dict_test)
key_true = dict_test.get('String2')
key_false = dict_test.get('TestString')
print('Получение значения по ключу "String2"', x)
print('Получение значения по ключу "TestString"', y)
