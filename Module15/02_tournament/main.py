# TODO здесь писать код
members = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
first_day = []
second_day = []

for count, member in enumerate(members):
    if count % 2 == 0:
        second_day.append(member)
    else:
        first_day.append(member)

print("Первый день: ", first_day, "\nВторой день: ", second_day)