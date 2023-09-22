import random
# numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]
numbers_list = []
max_index = 0
for _ in range(random.randrange(1, 15)):
    numbers_list.append(random.randint(1, 99))
print(f"Изначальный список: ", *numbers_list)

for index, num in enumerate(numbers_list):
    if num % 2 != 0:
        numbers_list.remove(num)
    max_index = len(numbers_list) - 1

for i in range(max_index):
    swap_num = numbers_list.pop(max_index)
    numbers_list.insert(i, swap_num)

print(f"Конечный список с разворотом: ", *numbers_list)
