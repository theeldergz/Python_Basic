goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


stock = [key for key in goods.keys()]
index_stock = 0
amount = 0
furn_count = 0


for furniture_id in goods.values():
    for item_id in store.keys():
        amount = 0
        furn_count = 0
        for count in range(len(store[item_id])):
            amount += store[item_id][count]['quantity'] * store[item_id][count]['price']
            furn_count += store[item_id][count]['quantity']
        if furniture_id == item_id:
            print("{name_furn} - {count} штук, стоимость {amount} рубля".format(
                name_furn=stock[index_stock],
                count=furn_count,
                amount=amount))
            index_stock += 1
