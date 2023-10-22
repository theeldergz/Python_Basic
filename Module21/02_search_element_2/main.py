site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def stock_deep(some_dict, deep=1):
    flag = False
    for _, value in some_dict.items():
        if isinstance(value, dict) and not flag:
            deep += stock_deep(value, deep)
            flag = True
    return deep


def search_dict(some_dict, search_value, deep):
    answer = None
    if deep >= 0:
        if search_value in some_dict:
            return some_dict[search_value]
        for key, value in some_dict.items():
            if isinstance(value, dict):
                answer = search_dict(value, search_value, (deep - 1))
                if answer:
                    return answer
    return answer


key = input("Введите искомый ключ: ").lower()
deep_choice = input("Хотите ввести максимальную глубину? Y/N: ").lower()
if deep_choice == 'y':
    deep = int(input("Введите максимальную глубину: "))
    answer = search_dict(site, key, deep)
    print("Значение ключа: ", answer)
else:
    max_deep = stock_deep(site)
    answer = search_dict(site, key, max_deep)
    print("Значение ключа: ", answer)

