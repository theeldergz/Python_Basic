import random

def points():
    point = random.uniform(5, 10)
    point = round(point, 2)
    return point


team1 = [points() for _ in range(20)]
print("\nПервая команда: ", team1)
team2 = [points() for _ in range(20)]
print("\nВторая команда: ",team2)

winners = [team1[i] if team1[i] > team2[i] else team2[i] for i in range(20)]
print("\nПобедители тура: ", winners)