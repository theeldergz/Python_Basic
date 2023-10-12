count = int(input("Введите количество пар слов: "))
pair_dict = {}

for i in range(count):
    pair = input(f"Введите пару номер {i + 1} (через пробел): ").lower().split()
    pair_dict[pair[0]], pair_dict[pair[1]] = pair[1], pair[0]

while True:
    get_synonym = input("Введите слово для проверки: ")
    if get_synonym in pair_dict:
        print(f'Синоним слова "{get_synonym}": ', pair_dict[get_synonym])
        break
    else:
        print("Такого слова нет в словаре, попробуйте еще раз!")
