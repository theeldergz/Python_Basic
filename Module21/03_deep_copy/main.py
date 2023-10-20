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
    new_site = copy.deepcopy(site)
    new_site['html']['head']['title'] = f'Куплю/продам {name_product} недорого'
    new_site['html']['body']['h2'] = f'У нас самая низкая цена на {name_product}'
    return new_site


site_count = int(input("Сколько сайтов: "))

for _ in range(site_count):
    phone_name = input("Введите название продукта для нового сайта: ")
    second_site = site_copy(site, phone_name)
    print(f'Сайт для {phone_name}: ')
    pprint.pprint(second_site)
