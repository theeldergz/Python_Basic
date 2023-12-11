import collections


def count_unique_characters(text: str) -> int:
    """ Функция находит кол-во уникальных элементов в строке text """
    return len(list(filter(lambda x: x == 1, collections.Counter(text.lower()).values())))


# Пример использования:
message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
