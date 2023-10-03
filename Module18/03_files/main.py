banned_symbols = "@№$%^&\*()"
banned_extensions = [".txt", ".docx"]
flag_banned_sym = False
flag_banned_ext = True

user_input = input("Введите название файла: ")

for sym in banned_symbols:
    if user_input.startswith(sym):
        flag_banned_sym = True

for ext in banned_extensions:
    if user_input.endswith(ext):
        flag_banned_ext = False


if flag_banned_sym:
    print("Ошибка: название начинается на один из специальных символов.")
elif flag_banned_ext:
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx.")
else:
    print("Файл назван верно.")
