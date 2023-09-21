# TODO здесь писать код

def min_divider(num):
    min_div = 2
    for div in range(2, num + 1):
        if num % div == 0:
           return div


x = int(input("Введите число: "))
x = min_divider(17)

print(x)