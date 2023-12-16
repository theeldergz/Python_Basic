import json
import pprint

diff_list = ["services", "staff", "datetime"]
temp_dict = dict()

with open('result.json', 'w+', encoding='utf-8') as result, open('json_old.json') as old, open('json_new.json') as new:
    old_data = json.loads(old.read())
    new_data = json.loads(new.read())
    print('\nСтарый файл:')
    pprint.pprint(old_data,  indent=4)
    print('\nНовый файл:')
    pprint.pprint(new_data, indent=4)
    for diff in diff_list:
        if old_data['data'][diff] != new_data['data'][diff]:
            temp_dict[diff] = new_data['data'][diff]

    json.dump(temp_dict, result, indent=4)

print('\nResult:')
pprint.pprint(temp_dict, indent=4)
