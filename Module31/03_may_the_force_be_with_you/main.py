import requests
import json
import pprint

my_req = requests.get('https://swapi.dev/api/starships/10/')
data = json.loads(my_req.text)
pilots_list = data['pilots']
new_pilots_list = list()

for pilot in pilots_list:
    pilot_data = json.loads(requests.get(pilot).text)
    new_pilots_list.append(pilot_data)

data['pilots'] = new_pilots_list

with open('starship_req.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)

pprint.pprint(data, indent=4)
