class Parent:

    def __init__(self, name, age, *args):
        self.name = name
        self.age = age
        self. children = args

    def info(self):
        print(f'\n\nName: {self.name}\nAge: {self.age}\nChildren: {self.children}')

    def baby_chill(self, one_of_child):
        if one_of_child.chill_status == 3:
            print('Ребенок не хочет играть!')
        else:
            one_of_child.chill_status += 1
            print('Ребенку уделили время')

    def baby_food(self, one_of_child):
        if one_of_child.food_status == 3:
            print('Ребенок не хочет есть!')
        else:
            one_of_child.food_status += 1
            print('Ребенка покормили')


class Child:

    def __init__(self, name, age, parent, food_status=0, chill_status=0):
        self.name = name
        self.age = age
        self.food_status = food_status
        self.chill_status = chill_status
        self.parent = parent

        if self.age > (parent.age - 16):
            raise ValueError("Ошибка: Ребенок не может быть такого возраста")

    def food_status_info(self):
        if self.food_status == 0:
            print(f'{self.name} Необходимо срочно покормить!')
        elif self.food_status == 1:
            print(f'{self.name} Очень голоден')
        elif self.food_status == 2:
            print(f'{self.name} Немного голоден')
        elif self.food_status == 3:
            print(f'{self.name} Полностью сыт')

    def chill_status_info(self):
        if self.chill_status == 0:
            print(f'{self.name} Плачет')
        elif self.chill_status == 1:
            print(f'{self.name} Сильно обеспокоен')
        elif self.chill_status == 2:
            print(f'{self.name} Немного обеспокоен')
        elif self.chill_status == 3:
            print(f'{self.name} Счастлив')

    def print_status(self):
        print(f'\nСостояние спокойствия {self.name}: ', end='')
        self.chill_status_info()
        print(f'Состояние сытости {self.name}: ', end='')
        self.food_status_info()


def create():
    child_list = []

    parent_name = input('Укажите имя родителя: ')
    parent_age = int(input('Укажите возраст родителя: '))
    baby_list = input('Укажите список детей через пробел: ').split()

    new_parent = Parent(parent_name, parent_age, baby_list)

    for baby in baby_list:
        baby_age = int(input(f'Укажите возраст {baby}: '))
        new_child = Child(baby, baby_age, new_parent)
        child_list.append(new_child)
    return new_parent, child_list
def menu():
    menu_choice = int(input('Нажмите 1 чтобы войти в меню создания семьи\nНажмите любую другую кнопку для выхода: '))
    if menu_choice == 1:
        new_parent, child_list = create()
        while True:
            select = int(input('\n\nЧто вы хотите сделать?'
                               '\n\t1.Посмотреть информацию о родителе'
                               '\n\t2.Посмотреть информацию о детях'
                               '\n\t3.Поиграть с детьми'
                               '\n\t4.Покормить детей'
                               '\n\tЛюбую другую клавишу для выхода:  '))
            if select == 1:
                new_parent.info()
            elif select == 2:
                for baby in child_list:
                    baby.print_status()
            elif select == 3:
                for baby in child_list:
                    new_parent.baby_chill(baby)
            elif select == 4:
                for baby in child_list:
                    new_parent.baby_food(baby)
            else:
                print('Выход из меню')
                break

    else:
        raise BaseException('Выход из программы!')


menu()

