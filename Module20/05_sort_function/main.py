# def tpl_sort(some_tuple):
#     frozen_sm_tpl = some_tuple
#     some_tuple = list(some_tuple)
#     for num1 in range(len(some_tuple) - 1):
#         for num2 in range(len(some_tuple) - 1):
#             if some_tuple[num2] > some_tuple[num2 + 1]:
#                 temp = some_tuple[num2]
#                 some_tuple[num2] = some_tuple[num2 + 1]
#                 some_tuple[num2 + 1] = temp
#             elif some_tuple[num2] % 1 != 0:
#                 return frozen_sm_tpl
#     some_tuple = tuple(some_tuple)
#     return some_tuple
#



def tpl_sort(some_tuple):
    is_unit = True
    for index, value in enumerate(some_tuple):
        if value % 1 != 0:
            is_unit = False

    if is_unit:
        return tuple(sorted(some_tuple))
    return some_tuple

test1 = (0.2, 6, 3, -1, 8, 4.6, 4, 10, -5)
test2 = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(test1))
print(tpl_sort(test2))