import random
# numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]
numbers_list = []
max_index = 0
index_in_numlist = 0
for _ in range(random.randrange(1, 15)):
    numbers_list.append(random.randint(1, 99))
print(f"Изначальный список: ", *numbers_list)


while index_in_numlist < len(numbers_list):
    if numbers_list[index_in_numlist] % 2 != 0:
        numbers_list.pop(index_in_numlist)
    else:
        index_in_numlist += 1
# for index, num in enumerate(numbers_list):
#     if num % 2 != 0:
#         numbers_list.remove(num)
#     max_index = len(numbers_list) - 1

for i in range(max_index):
    swap_num = numbers_list.pop(max_index)
    numbers_list.insert(i, swap_num)

print(f"Конечный список с разворотом: ", *numbers_list)
