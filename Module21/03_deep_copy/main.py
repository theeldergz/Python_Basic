import copy
import pprint
site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def site_copy(site_reference, name_product):
    second_site = copy.deepcopy(site_reference)
    second_site['html']['head']['title'] = f'Куплю/продам {name_product} недорого'
    second_site['html']['body']['h2'] = f'У нас самая низкая цена на {name_product}'
    return second_site


site_count = int(input("Сколько сайтов: "))

new_sites = {}

for _ in range(site_count):
    phone_name = input("Введите название продукта для нового сайта: ")
    site_header = f'Сайт для {phone_name}'
    new_sites[site_header] = site_copy(site, phone_name)
    for key, value in new_sites.items():
        print(key)
        pprint.pprint(value)



