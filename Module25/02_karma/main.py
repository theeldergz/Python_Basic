import random

EXC_LIST = ['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError', None]
NEED_KARMA = 0


def one_day():
    data = random.choices(EXC_LIST, weights=[0.02, 0.02, 0.02, 0.02, 0.02, 0.9])
    try:
        if data[0] is None:
            return random.randint(1, 7)
        else:
            with open('karma.log', 'a') as karma_logs:
                line = '\n' + str(ValueError(data[0]))
                karma_logs.write(line)
                raise ValueError(data[0])

    except ValueError:
        return 0


while NEED_KARMA <= 500:
    NEED_KARMA += one_day()



