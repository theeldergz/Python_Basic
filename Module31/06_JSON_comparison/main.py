import json
import pprint
from typing import Generator


def generate_all_items(structure: dict) -> Generator:
    if isinstance(structure, dict):
        for key, elem in structure.items():
            yield key, elem
            yield from generate_all_items(elem)
    elif isinstance(structure, list):
        for elem in structure:
            yield from generate_all_items(elem)


def search_diff(old_data: json, new_data: json, target_tags: list) -> dict:
    def check_pair(first_pair, second_pair):
        return first_pair[0] in target_tags and first_pair != second_pair

    return {second_pair[0]: second_pair[1]
            for first_pair, second_pair in zip(generate_all_items(old_data), generate_all_items(new_data))
            if check_pair(first_pair, second_pair)}


def main():
    with open('result.json', 'w+', encoding='utf-8') as result, open('json_old.json') as old, \
            open('json_new.json') as new:

        diff_list = ["services", "staff", "datetime"]
        old_data = json.loads(old.read())
        new_data = json.loads(new.read())

        diff_elem = search_diff(old_data, new_data, diff_list)

        pprint.pprint(diff_elem, indent=4)
        json.dump(diff_elem, result, indent=4)


if __name__ == '__main__':
    main()
