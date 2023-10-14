def tpl_sort(some_tuple):
    frozen_sm_tpl = some_tuple
    some_tuple = list(some_tuple)
    for num1 in range(len(some_tuple) - 1):
        for num2 in range(len(some_tuple) - 1):
            if some_tuple[num2] > some_tuple[num2 + 1]:
                temp = some_tuple[num2]
                some_tuple[num2] = some_tuple[num2 + 1]
                some_tuple[num2 + 1] = temp
            elif some_tuple[num2] % 1 != 0:
                return frozen_sm_tpl
    some_tuple = tuple(some_tuple)
    return some_tuple


print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))

