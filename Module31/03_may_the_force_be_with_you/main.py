import requests
import json
import pprint

if __name__ == '__main__':
    ship = dict()
    temp_list = list()

    ship_info = json.loads(requests.get('https://swapi.dev/api/starships/10/').text)
    ship['name'] = ship_info['name']
    ship['max_atmosphering_speed'] = ship_info['max_atmosphering_speed']
    ship['starship_class'] = ship_info['starship_class']
    ship['pilots'] = ship_info['pilots']

    for pilot_url in ship['pilots']:
        temp_dict = dict()
        pilot_info = json.loads(requests.get(pilot_url).text)
        temp_dict['name'] = pilot_info['name']
        temp_dict['height'] = pilot_info['height']
        temp_dict['mass'] = pilot_info['mass']
        temp_dict['homeworld_name'] = json.loads(requests.get(pilot_info['homeworld']).text)['name']
        temp_dict['homeworld'] = pilot_info['homeworld']
        temp_list.append(temp_dict)


    ship['pilots'] = [temp_list][0]

    with open('starship_req.json', 'w', encoding='utf-8') as json_file:
        json.dump(ship, json_file, indent=4)

    pprint.pprint(ship, indent=4, sort_dicts=False)



