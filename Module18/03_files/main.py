banned_symbols = ("@№$%^&\*()")
banned_extensions = (".txt", ".docx")
flag_banned_sym = False
flag_banned_ext = True

user_input = input("Введите название файла: ")

if user_input.startswith(banned_symbols):
    print('Ошибка: название начинается на один из специальных символов.')
elif not user_input.endswith(banned_extensions):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print("Файл назван верно.")
