# TODO здесь писать код
num = int(input("Введите число: "))
odd_num = []

for i in range(1, num + 1):
    if i % 2 != 0:
        odd_num.append(i)
print(odd_num)