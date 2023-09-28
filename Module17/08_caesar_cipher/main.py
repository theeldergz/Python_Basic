alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к',
            'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
            'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
def sym_index(sym):
    count = alphabet.index(sym)
    return count


text = input("Введите сообщение: ")
step = int(input("Введите сдвиг: "))

pressmark = [alphabet[(sym_index(sym) + step) % 33] if sym in alphabet else " " for sym in text ]

print(*pressmark)
