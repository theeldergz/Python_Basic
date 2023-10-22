import copy

nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def unpacker(some_list, summary=[]):
    for elem in some_list:
        if isinstance(elem, list):
            unpacker(elem)
        else:
            summary.append(elem)
    return summary




def unpack(test_list):
    some_list = unpacker(test_list)
    second_list = some_list
    result_list = copy.deepcopy(second_list)
    second_list.clear()
    return result_list

print(unpack(nice_list))
print(unpack(nice_list))
