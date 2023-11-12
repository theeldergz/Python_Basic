import random


class Human:
    def __init__(self, name, house, satiety=50):
        self.name = name
        self.house = house
        self.satiety = satiety

    def eat(self, house):
        self.satiety += 10
        self.house.food -= 10

    def work(self, house):
        roll_money = random.randint(5, 20)
        house.money += roll_money
        house.all_money += roll_money
        self.satiety -= 10

    def play(self, house):
        self.satiety -= 10
        house.count_play_games += 1

    def market(self, house):
        house.food += 20
        house.money -= 10
        house.all_food += 20

    def one_day(self, house, day):
        print(f'\n{self.name} проживает свой {day} день!')
        print(f'{self.name}: Сытость: {self.satiety}')
        print(f'Eда в доме: {house.food}\nДеньги в доме:{house.money}')
        print(f'\tБыло заработано: {house.all_money}'
              f'\n\tБыло куплено еды за все время:{house.all_food}'
              f'\n\tСыграно в игры за все время: {house.count_play_games}')

        roll = random.randint(1, 6)

        if self.satiety <= 0:
            raise ValueError(f'{self.name} Умер!!!')

        if self.satiety < 20:
            self.eat(house)
        elif house.food < 10:
            self.market(house)
        elif house.money < 50:
            self.work(house)
        elif roll == 1:
            self.work(house)
        elif roll == 2:
            self.eat(house)
        else:
            self.play(house)


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
    human1.one_day(test_house, day)
    human2.one_day(test_house, day)
