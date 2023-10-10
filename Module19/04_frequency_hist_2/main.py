text = input("Введите текст: ")
sym_dict = {}

for sym in text:
    if sym in sym_dict:
        sym_dict[sym] += 1
    else:
        sym_dict[sym] = 1

keys = sym_dict.keys()

print("Оригинальный словарь частот: ")
for sym in sym_dict:
    print(sym, ":", sym_dict[sym])

values = set(sym_dict.values())

print("Инвертированный словарь частот:")
for index in values:
    sym_list = list()
    answer_dict = dict()
    for sym_2 in sym_dict:
        if index == sym_dict[sym_2]:
            sym_list.append(sym_2)
    answer_dict[index] = sym_list
    print(*answer_dict, ":", answer_dict[index])
