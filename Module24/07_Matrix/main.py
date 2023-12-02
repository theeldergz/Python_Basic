import copy


class Matrix:
    def __init__(self, fields, strings, data=None):
        self.fields = fields
        self.strings = strings

        if data is None:
            self.data = [[None for _ in range(strings)] for _ in range(fields)]
        else:
            self.data = data

    def __str__(self):
        value = str()

        for sub_list in self.data:
            value += '\n\n'
            for num in sub_list:
                value += str(num) + '	'

        return value

    def add(self, other_matrix):
        other_matrix_data = copy.deepcopy(other_matrix.data)
        self_data = copy.deepcopy(self.data)

        for i, value_1 in enumerate(self_data):
            for j, value_2 in enumerate(self_data[i]):
                other_matrix_data[i][j] += self_data[i][j]

        value = str()

        for sub_list in other_matrix_data:
            value += '\n\n'
            for num in sub_list:
                value += str(num) + '	'

        return value

    def subtract(self, other_matrix):
        other_matrix_data = copy.deepcopy(other_matrix.data)
        self_data = copy.deepcopy(self.data)

        for i, value_1 in enumerate(self_data):
            for j, value_2 in enumerate(self_data[i]):
                self_data[i][j] -= other_matrix_data[i][j]

        value = str()

        for sub_list in self_data:
            value += '\n\n'
            for num in sub_list:
                value += str(num) + '	'

        return value

    def multiply(self, other_matrix):
        other_matrix_data = copy.deepcopy(other_matrix.data)
        self_data = copy.deepcopy(self.data)

        try:
            for i, value_1 in enumerate(self_data):
                for j, value_2 in enumerate(self_data[i]):
                    self_data[i][j] *= other_matrix_data[i][j]

        except IndexError as exc:
            print('Неподходящий форомат матрицы, будет выполнено транспонирование: ')
            self_data.clear()

        finally:
            other_matrix_template = [[None for _ in range(other_matrix.strings)] for _ in range(other_matrix.fields)]
            self_data = copy.deepcopy(self.data)

            for i, value_1 in enumerate(self_data):
                for j, value_2 in enumerate(self_data[i]):
                    other_matrix_template[j][i] = self_data[i][j]

            for i, value_1 in enumerate(other_matrix_template):
                for j, value_2 in enumerate(other_matrix_template[i]):
                    other_matrix_template[i][j] *= other_matrix_data[i][j]

            value = str()

            for sub_list in other_matrix_template:
                value += '\n\n'
                for num in sub_list:
                    value += str(num) + '	'

            return value

    def transpose(self):
        result = [[None for _ in range(self.fields)] for _ in range(self.strings)]

        for i, value_1 in enumerate(self.data):
            for j, value_2 in enumerate(self.data[i]):
                result[j][i] = self.data[i][j]

        value = str()

        for sub_list in result:
            value += '\n\n'
            for num in sub_list:
                value += str(num) + '	'

        return value










# Примеры работы с классом:

# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("\nСложение матриц:")
print(m1.add(m2))

print("\nВычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("\nУмножение матриц:")
print(m1.multiply(m3))

print("\nТранспонирование матрицы 1:")
print(m1.transpose())