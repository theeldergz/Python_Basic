import collections


def can_be_poly(text : str) -> bool:
    """ Однострочник, проверяет, можно ли создать палиндром из text  """
    return len(list(filter(lambda x: x % 2, collections.Counter(text).values()))) <= 2


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))

