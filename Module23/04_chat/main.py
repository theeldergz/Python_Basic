user_dict = {}


def menu():
    try:
        menu_choice = int(input("\nМеню чата:\n1.Залогиниться\n2.Выйти!\n\n"))

        if menu_choice == 1:
            current_user = login()
            while True:
                current_choice = int(input("\n1.Ввести сообщение\n2.Показать историю\n"))
                if current_choice == 1:
                    print('напишите "Выход" чтобы выйти')
                    current_message = ''
                    while current_message.lower() != 'выход':
                        current_message = input('$ ')
                        new_message(current_user, current_message)
                elif current_choice == 2:
                    check_history()

    except ValueError:
        print("\nНеверно введена команда из меню\n")
        print('Попробуйте снова!\n')


def login():
    try:
        user = input("Просьба ввести ваш логин: ")

        if user in user_dict:
            password = input("Введите пароль: ")
            if user_dict[user] == password:
                print(f'Добрый день {user}!')
                return user
            else:
                raise ValueError
        else:
            password_new = input("Придумайте пароль: ")
            user_dict.setdefault(user, password_new)
            print(f'Добрый день {user}!')
            return user
    except ValueError:
        print("\nВы не прошли проверку!\n")


def new_message(user, msg):
    with open('chat.log', 'a', encoding='utf-8') as chat_history:
        chat_history.write('\n')
        chat_history.write(user)
        chat_history.write(' написал:\t')
        chat_history.write(msg)


def check_history():
    with open('chat.log', 'r', encoding='utf-8') as chat_history:
        history = chat_history.read()
        print(history)


menu()
