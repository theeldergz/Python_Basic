array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
array_x = []


for num in array_1:
    if num in array_2 and num in array_3:
       array_x.append(num)

print("Задача номер 2")
print("\n\tРешение без set: ", *array_x)
print("\tРешение с set: ", *set(array_1) & set(array_2) & set(array_3))


array_x.clear()
for num in array_1:
    if num not in array_2 and num not in array_3:
       array_x.append(num)

array_1_set = set(array_1)
array_1_set -= set(array_2)
array_1_set -= set(array_3)

print("\nЗадача номер 1")
print("\n\tРешение без set: ", *array_x)
print("\tРешение с set: ", *array_1_set)

