list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]

for i in list1:
    for j in list2:
        if i == j:
            list1.remove(i)
list1.extend(list2)
list1.sort()

print(*list1)