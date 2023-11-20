import random


class KillError(Exception):
    def __init__(self):
        super().__init__('Вы убили человека!')


class DrunkError(Exception):
    def __init__(self):
        super().__init__('Вы напились!')


class CarCrashError(Exception):
    def __init__(self):
        super().__init__('Вы попали в дтп!')


class GluttonyError(Exception):
    def __init__(self):
        super().__init__('Вы обьелись!')


class DepressionError(Exception):
    def __init__(self):
        super().__init__('Депрессия...')


NEED_KARMA = 0


def one_day():
    exceptions = random.choice((KillError, DrunkError, CarCrashError, GluttonyError, DepressionError))
    try:
        if random.randint(1, 10) == 7:
            raise exceptions
        else:
            return random.randint(1, 7)

    except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as exc:
        print(exc)


while NEED_KARMA <= 500:
    try:
        NEED_KARMA += one_day()
    except TypeError:
        pass
else:
    print('\nВы успешно прожили жизнь не смотря на все неудачи!!!')