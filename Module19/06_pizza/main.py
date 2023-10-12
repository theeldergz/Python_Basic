guests_orders = {}

order_count = int(input("Введите колво заказов: "))

for index_info in range(order_count):
    guest, pizza_name, count = input(f"Введите {index_info + 1} заказ(через пробел): ").lower().split()
    count = int(count)
    if guest not in guests_orders:
        guests_orders[guest] = {pizza_name: count}
    elif pizza_name not in guests_orders[guest]:
        guests_orders[guest][pizza_name] = count
    else:
        guests_orders[guest][pizza_name] += count

guests_orders_name = [key for key in guests_orders.keys()]
guests_orders_name.sort()

for guest_name in guests_orders_name:
    guests_orders_pizza = [key for key in guests_orders[guest_name].keys()]
    print(guest_name.capitalize(), ": ")
    guests_orders_pizza.sort()
    for pizza in guests_orders_pizza:
        print("\t", pizza.capitalize(), ": ", guests_orders[guest_name][pizza])

