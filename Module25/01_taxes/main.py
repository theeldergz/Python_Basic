class Property:

    def __init__(self, worth, percent=0.008):
        self.percent = percent
        self.worth = worth

    def tax_calc(self):
        taxes = int(self.worth) * self.percent
        taxes = round(taxes)
        return taxes


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth, percent=0.001)
        self.worth = worth


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth, percent=0.005)
        self.worth = worth


def calculated(input_money, input_property):
    if money >= input_property.tax_calc():
        print(f'\nВы оплатили налог в размере {input_property.tax_calc()}!')
        print(f'Осталось денег: {money - input_property.tax_calc()}')
    else:
        need_money = input_property.tax_calc() - input_money
        print(f'\nНеобходимо еще {need_money} для оплаты!')


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth, percent=0.002)
        self.worth = worth


while True:
    money = int(input('\nВведите кол-во имеющихся денег: '))
    property_choice = int(input('\nВыберите имущество за которое хотите заплатить налог:'
                                '\n\t1.Квартира\n\t2.Машина\n\t3.Загородный дом\nВыберите пункт: '))

    if property_choice == 1:
        property_worth = int(input('\nВведите стоимость кваритры: '))
        apart = Apartment(property_worth)
        calculated(money, apart)
        break

    elif property_choice == 2:
        property_worth = int(input('\nВведите стоимость машины: '))
        car = Car(property_worth)
        calculated(money, car)
        break

    elif property_choice == 3:
        property_worth = int(input('\nВведите стоимость загородного дома: '))
        house = CountryHouse(property_worth)
        calculated(money, house)
        break
