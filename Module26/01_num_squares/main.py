limit_num = int(input('Пожалуйста введите число: '))

class Square:
    def __init__(self, limit):
        self.limit = limit
        self.square_num = 0

    def __next__(self):
        while self.square_num < self.limit:
            self.square_num += 1
            return self.square_num ** 2
        raise StopIteration

    def __iter__(self):
        return self


test_square = Square(limit_num)
print('При помощи итератора: ')
for num in test_square:
    print(num)


def test_gen(limit):
    square_num = 0
    while square_num < limit:
        square_num += 1
        yield square_num ** 2


test_func_gen = test_gen(limit_num)
print('\nПри помощи функции генератора: ')
for num2 in test_func_gen:
    print(num2)

test_gen_frase = (num ** 2 for num in range(1, limit_num + 1))
print('\nПри помощи генераторного выражения: ')
for num3 in test_gen_frase:
    print(num3)
