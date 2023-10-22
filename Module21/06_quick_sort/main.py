def list_sep(some_list):
    base_elem = []
    higher_elem = []
    lower_elem = []
    for elem in some_list:
        if elem > some_list[-1]:
            higher_elem.append(elem)
        elif elem == some_list[-1]:
            base_elem.append(elem)
        elif elem < some_list[-1]:
            lower_elem.append(elem)

    return lower_elem, base_elem, higher_elem


def fast_sort(some_list):
    bot, mid, top = list_sep(some_list)

    if top:
        top = fast_sort(top)
    if bot:
        bot = fast_sort(bot)

    result_list = [*bot, *mid, *top]
    return result_list

testlist = [1, 5, 5, 2, 7, 2, 7, 6, 9, 12, 4, 23, 2, 6]
test = fast_sort(testlist)
print(test)

