import random


class Hero:
    # Базовый класс, который не подлежит изменению
    # У каждого наследника будут атрибуты:
    # - Имя
    # - Здоровье
    # - Сила
    # - Жив ли объект
    # Каждый наследник будет уметь:
    # - Атаковать
    # - Получать урон
    # - Выбирать действие для выполнения
    # - Описывать своё состояние

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    # Все наследники должны будут переопределять каждый метод базового класса (кроме геттеров/сеттеров)
    # Переопределенные методы должны вызывать методы базового класса (при помощи super).
    # Методы attack и __str__ базового класса можно не вызывать (т.к. в них нету кода).
    # Они нужны исключительно для наглядности.
    # Метод make_a_move базового класса могут вызывать только герои, не монстры.
    def attack(self, target):
        # Каждый наследник будет наносить урон согласно правилам своего класса
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    def take_damage(self, damage):
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ", round(self.get_hp()))
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять стратегию, чтобы улучшить выживаемость героев
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        # Каждый наследник должен выводить информацию о своём состоянии, чтобы вы могли отслеживать ход сражения
        raise NotImplementedError("Вы забыли переопределить метод __str__!")


class Healer(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.__magic_power = super().get_power() * 3

    def is_alive(self):
        return super().is_alive()

    def attack(self, target):
        target.take_damage(self.get_power() // 2)

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - (damage * 1.2))
        super().take_damage(damage * 1.2)

    def heal(self, target):
        target.set_hp(target.get_hp() + self.__magic_power)
        print(f'Я хиллер {self.name} лечу союзника(ов) на {target.get_hp() + self.__magic_power}')

    def make_a_move(self, friends, enemies):
        for hero in friends:
            if hero.get_hp() <= 150:
                self.heal(hero)

        super().make_a_move(friends, enemies)

    def __str__(self):
        info = str(f'Я {self.name}, живой: {self.is_alive()}, мое кол-во xp: {super().get_hp()}')
        return info

    # Целитель:
    # Атрибуты:
    # - магическая сила - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3 (self.__power * 3)
    # Методы:
    # - атака - может атаковать врага, но атакует только в половину силы self.__power
    # - получение урона - т.к. защита целителя слаба - он получает на 20% больше урона (1.2 * damage)
    # - исцеление - увеличивает здоровье цели на величину равную своей магической силе
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # исцеление) на выбранную им цель


class Tank(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.__guard = True
        self.__defence = 1

    def is_alive(self):
        return super().is_alive()

    def attack(self, target):
        target.take_damage(self.get_power() // 2)

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - (damage // self.__defence))
        super().take_damage(damage // self.__defence)


    def shield_up(self):
        if not self.__guard:
            print('Поднять щиты!!!')
            self.__defence *= 2
            self.set_power(self.get_power() // 2)

    def shield_down(self):
        if self.__guard:
            print('Опускаем щиты!!!')
            self.__defence /= 2
            self.set_power(self.get_power() * 2)

    def make_a_move(self, friends, enemies):
        if self.get_hp() <= 350:
            self.shield_up()
        else:
            self.shield_down()
        super().make_a_move(friends, enemies)

    def __str__(self):
        info = str(f'Я {self.name}, живой: {self.is_alive()}, мое кол-во xp: {super().get_hp()}')
        return info
    # Танк:
    # Атрибуты:
    # - показатель защиты - изначально равен 1, может увеличиваться и уменьшаться
    # - поднят ли щит - танк может поднимать щит, этот атрибут должен показывать поднят ли щит в данный момент
    # Методы:
    # - атака - атакует, но т.к. доспехи очень тяжелые - наносит половину урона (self.__power)
    # - получение урона - весь входящий урон делится на показатель защиты (damage/self.defense) и только потом отнимается от здоровья
    # - поднять щит - если щит не поднят - поднимает щит. Это увеличивает показатель брони в 2 раза, но уменьшает показатель силы в 2 раза.
    # - опустить щит - если щит поднят - опускает щит. Это уменьшает показатель брони в 2 раза, но увеличивает показатель силы в 2 раза.
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # поднять щит/опустить щит) на выбранную им цель


class Attacker(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.__power_multiply = 1

    def is_alive(self):
        return super().is_alive()

    def attack(self, target):
        target.take_damage(self.get_power() * self.__power_multiply)

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - (self.__power_multiply // 2))
        super().take_damage(damage)

    def power_down(self):
        self.__power_multiply //= 2

    def power_up(self):
        self.__power_multiply *= 2

    def make_a_move(self, friends, enemies):
        self.attack(enemies[0])
        print(f"Я Убийца {self.name} Атакую того, кто стоит ближе -", enemies[0].name,
              f"наношу урон равный: {self.get_power()}")
        super().make_a_move(friends, enemies)

    def __str__(self):
        info = str(f'Я {self.name}, живой: {self.is_alive()}, мое кол-во xp: {super().get_hp()}')
        return info

    # Убийца:
    # Атрибуты:
    # - коэффициент усиления урона (входящего и исходящего)
    # Методы:
    # - атака - наносит урон равный показателю силы (self.__power) умноженному на коэффициент усиления урона (self.power_multiply)
    # после нанесения урона - вызывается метод ослабления power_down.
    # - получение урона - получает урон равный входящему урона умноженному на половину коэффициента усиления урона - damage * (
    # self.power_multiply / 2)
    # - усиление (power_up) - увеличивает коэффициента усиления урона в 2 раза
    # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # усиление, ослабление) на выбранную им цель
