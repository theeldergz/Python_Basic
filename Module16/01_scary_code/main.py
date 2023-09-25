a_list = [1, 5, 3]
b_list = [1, 5, 1, 5]
c_list = [1, 3, 1, 5, 3, 3]

a_list.extend(b_list)
count_five = a_list.count(5)

for _ in range(count_five):
    a_list.remove(5)

a_list.extend(c_list)
count_three = a_list.count(3)

print(f"\nКол-во цифр 5 при первом объединении: {count_five}\nКол-во цифр 3 при втором объединении: {count_three}\nИтоговый список: {a_list}")
