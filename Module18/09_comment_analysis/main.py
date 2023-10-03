def count_uppercase_lowercase(text):
    upper_count = 0
    lower_count = 0
    for sym in text:
        if sym.isupper():
            upper_count +=1
        if sym.islower():
            lower_count += 1
    return upper_count, lower_count


# Пример использования:
text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
