import random

random_list = [random.randint(1,99) for _ in range(10)]
# random_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

answer_list = [(random_list[index - 1], num1) for index, num1 in enumerate(random_list) if index % 2 != 0]

#не забыть про zip
print(random_list)
print(answer_list2)

