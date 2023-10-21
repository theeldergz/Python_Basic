import copy


def mid_summa(*args, summary=[]):
    some_list = args[0]

    if isinstance(args[0], int):
        sec_sum = [num for num in args]
        summary.extend(sec_sum)
    else:
        for elem in some_list:
            if isinstance(elem, list):
                mid_summa(elem)
            else:
                summary.append(elem)

    return summary


def summa(*args):
    second_list = mid_summa(args)
    testlist = copy.deepcopy(second_list)
    summ = sum(testlist)
    second_list.clear()
    return summ


print(summa([[1, 2, [3]], [1], 3]))
print(summa(1, 2, 3, 4, 5))
