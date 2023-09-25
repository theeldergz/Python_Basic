shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

total_Amount = 0
count_detail_in_stock = 0

detail_choice = input("Название детали: ")

for detail in shop:
        if detail_choice.lower() == detail[0]:
                total_Amount += detail[1]
                count_detail_in_stock += 1
print("Кол-во деталей: ", count_detail_in_stock)
print("Общая стоимость: ", total_Amount)
