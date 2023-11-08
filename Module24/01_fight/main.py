import random


class Warrior:
    def __init__(self, name="fighter", attack=20, health=100):
        self.health = health
        self.attack = attack
        self.name = name

    def attack_enemy(self, enemy):
        enemy.health -= self.attack
        print(f'{self.name} атакует врага {enemy.name}!' )
        print(f'\tУ {enemy.name} осталось: {enemy.health} здоровья\n')


def battle(fighter_1, fighter_2):
    battle_list = [fighter_1, fighter_2]

    while True:
        first_punch = random.choice(battle_list)
        for fighter in battle_list:
            if fighter != first_punch:
                first_punch.attack_enemy(fighter)
        if fighter_1.health <= 0:
            print(f"\n\tПобедителем стновится {fighter_2.name}")
            break
        elif fighter_2.health <= 0:
            print(f"\n\tПобедителем стновится {fighter_1.name}")
            break


war1 = Warrior('Spartak')
war2 = Warrior('Krics')

battle(war1, war2)



