import random


class Human:
    def __init__(self, name, house, satiety=50):
        self.name = name
        self.house = house
        self.satiety = satiety

    def eat(self):
        self.satiety += 10
        self.house.food -= 10

    def work(self):
        roll_money = random.randint(5, 20)
        self.house.money += roll_money
        self.house.all_money += roll_money
        self.satiety -= 10

    def play(self):
        self.satiety -= 10
        self.house.count_play_games += 1

    def market(self):
        self.house.food += 20
        self.house.money -= 10
        self.house.all_food += 20

    def one_day(self, day):
        print(f'\n{self.name} проживает свой {day} день!')
        print(f'{self.name}: Сытость: {self.satiety}')
        print(f'Eда в доме: {self.house.food}\nДеньги в доме:{self.house.money}')
        print(f'\tБыло заработано: {self.house.all_money}'
              f'\n\tБыло куплено еды за все время:{self.house.all_food}'
              f'\n\tСыграно в игры за все время: {self.house.count_play_games}')

        roll = random.randint(1, 6)

        if self.satiety <= 0:
            raise ValueError(f'{self.name} Умер!!!')

        if self.satiety < 20:
            self.eat()
        elif self.house.food < 10:
            self.market()
        elif self.house.money < 50:
            self.work()
        elif roll == 1:
            self.work()
        elif roll == 2:
            self.eat()
        else:
            self.play()


class House:
    all_money = 0
    all_food = 0
    count_play_games = 0

    def __init__(self, food=50, money=0):
        self.food = food
        self.money = money


test_house = House()
human1 = Human('Denis', test_house)
human2 = Human('Sasha', test_house)

for day in range(1, 366):
    human1.one_day(day)
    human2.one_day(day)
