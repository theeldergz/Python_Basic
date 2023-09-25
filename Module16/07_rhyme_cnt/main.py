N = int(input("Кол-во игроков: "))
K = int(input("Какое число в считалке?  "))
player_list = list(range(1, N + 1))

for _ in range(N - 1):
    print("Текущий круг людей: ", player_list)
    num = int(input("Начало счета с номера: "))

    lenght = len(player_list)
    dash = K % lenght
    index = player_list.index(num)
    del_human = player_list[index + dash - 1]
    player_list.remove(del_human)

    print("Выбыл ", del_human)

print("\n\tПобедил ", *player_list)

