guests_orders = {}



order_count = int(input("Введите колво заказов: "))

for index_info in range(order_count):
    order = input(f"Введите {index_info + 1} заказ(через пробел): ").lower().split()
    order[2] = int(order[2])
    if order[0] not in guests_orders:
        guests_orders[order[0]] = {order[1]: order[2]}
    elif order[1] not in guests_orders[order[0]]:
        guests_orders[order[0]][order[1]] = order[2]
    else:
        guests_orders[order[0]][order[1]] += order[2]

guests_orders_name = [key for key in guests_orders.keys()]
guests_orders_name.sort()


for guest in guests_orders_name:
    guests_orders_pizza = [key for key in guests_orders[guest].keys()]
    print(guest.capitalize(), ": ")
    guests_orders_pizza.sort()
    for pizza in guests_orders_pizza:
        print("\t", pizza.capitalize(), ": ", guests_orders[guest][pizza])

