import json
import pprint
from typing import Any

diff_list = ["services", "staff", "datetime"]
temp_dict = list()


def key_search(data: dict, req_key: str) -> list[str | Any] | Any:
    """ Рекурсивная функция. Ищет значение по ключу req_key и сохраняет его в temp_value, и возвращает """
    temp_value = {req_key: ''}
    if isinstance(data, dict):
        for key, value in data.items():
            if key == req_key:
                return value
            else:
                temp_1 = (key_search(value, req_key))
                if temp_1:
                    temp_value[req_key] = temp_1
    elif isinstance(data, list):
        for elem in data:
            temp_2 = (key_search(elem, req_key))
            if temp_2:
                temp_value[req_key] = temp_2
    return temp_value


with open('result.json', 'w+', encoding='utf-8') as result, open('json_old.json') as old, open('json_new.json') as new:
    old_data = json.loads(old.read())
    new_data = json.loads(new.read())
    print('\nСтарый файл:')
    pprint.pprint(old_data, indent=4)
    print('\nНовый файл:')
    pprint.pprint(new_data, indent=4)
    for diff in diff_list:
        old_value = json.dumps(key_search(old_data, diff))
        new_value = json.dumps(key_search(new_data, diff))
        if old_value != new_value:
            json.dump(key_search(new_data, diff), result, indent=4)
            print('\nСтарое значение: ')
            pprint.pprint(old_value, indent=4)
            print('\nНовое значение: ')
            pprint.pprint(new_value, indent=4)
