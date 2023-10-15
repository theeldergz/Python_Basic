test_string = 'abcd'
test_tuple = (10, 20, 30, 40)


def genexpr(iter1, iter2):
    if len(iter1) < len(iter2):
        return ((obj, iter2[index]) for index, obj in enumerate(iter1))
    return ((iter1[index], obj) for index, obj in enumerate(iter2))


print(genexpr(test_string, test_tuple))
print(*genexpr(test_string, test_tuple))
