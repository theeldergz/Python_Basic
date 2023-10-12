sym_dict = {}
even_count = 0
odd_count = 0

palindrom = input("Введите строку: ")

for sym in palindrom:
    sym_dict[sym] = sym_dict.get(sym, 0) + 1

for key in sym_dict.values():
    if key % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

if odd_count != 1:
    print("Нельзя сделать палиндромом")
else:
    print("Можно сделать палиндромом")


