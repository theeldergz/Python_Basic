text = input("Введите текст: ")

vowels = ['а', 'о', 'у', 'и', 'э', 'ы', 'е', 'ё', 'я', 'ю']
symbols = [sym for sym in text if sym in vowels]
count_vowels = len(symbols)

print("Список гласных букв: ", symbols, "\nДлина списка: ", count_vowels)

