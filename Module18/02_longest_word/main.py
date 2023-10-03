user_input = input("Введите строку: ").split()

max_len = 0
max_word = None

for word in user_input:
    if max_len < len(word):
        max_len = len(word)
        max_word = word
    else:
        continue

print(f"Самое длинное слово: {max_word} \nДлина этого слова: {max_len}")
