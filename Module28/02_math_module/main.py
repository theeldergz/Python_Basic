import math


class MyMath:
    """ Класс отвечающий за мат. вычисления """
    @classmethod
    def circle_len(cls, radius: [float, int]) -> [float, int]:
        """ Вычисляет длину окружности """
        length = 2 * math.pi * radius
        return length

    @classmethod
    def circle_sq(cls, radius: [float, int]) -> [float, int]:
        """ Вычисляет площадь окружности """
        square = math.pi * radius ** 2
        return square

    @classmethod
    def volume_sph(cls, radius: [float, int]) -> [float, int]:
        """ Вычисляет обьем сферы """
        volume = 4 * math.pi * radius ** 2
        return volume

    @classmethod
    def volume_cube(cls, side: [float, int]) -> [float, int]:
        """ Вычисляет обьем куба """
        volume = side ** 3
        return volume


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.volume_sph(radius=7)
res_4 = MyMath.volume_cube(side=8)
print(res_1)
print(res_2)
print(res_3)
print(res_4)
