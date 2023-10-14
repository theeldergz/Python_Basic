user_dict = {}

while True:
    user_choice = int(input("""
    \nВведите номер действия: 
    1. Добавить контакт 
    2. Найти человека \n\t"""))

    if user_choice == 1:
        name = input("Введите имя и фамилию нового контакта (через пробел): ").lower().split()
        name = tuple(name)
        if name in user_dict:
            print("Такой человек уже есть в контактах.")
            print("Текущий словарь контактов: ", *user_dict)
            continue
        number = int(input("Введите номер телефона: "))
        user_dict.setdefault(name, number)

    elif user_choice == 2:
        user_info = input("Введите фамилию для поиска: ").lower()
        for dict_name, dict_surname in user_dict.keys():
            if user_info == dict_name or user_info == dict_surname:
                print(f'''Данные контакта "{user_info}":
                    \tИмя: "{str(dict_name).capitalize()}"
                    \tФамилия: "{str(dict_surname).capitalize()}"
                    \tНомер телефона: {user_dict[(dict_name, dict_surname)]}''')


