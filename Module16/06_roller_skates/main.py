size_N = []
size_K = []
count = 0
reserved = 0

count_skates = int(input("Кол-во коньков: "))

for size in range(1, count_skates + 1):
    size_N.append(int(input(f"Введите размер {size} пары: ")))

count_humans = int(input("Кол-во человек: "))

for human in range(1, count_humans +1):
    size_K.append(int(input(f"Размер ноги {human}-го человека : ")))
    if size_K[count] in size_N:
        size_N.remove(size_K[count])
        reserved += 1
    count += 1

print("Наибольшее кол-во людей, которые могут взять ролики: ", reserved)
