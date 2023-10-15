def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True


#
def crypto(iterator):
    crypto_list = []
    for index, value in enumerate(iterator):
        if is_prime(index):
            crypto_list.append(value)
    return crypto_list

print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))


