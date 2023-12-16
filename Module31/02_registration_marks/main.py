import re

test_number = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

tax_car = re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{5,6}', test_number)
person_car = re.findall(r'\b[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', test_number)

print('Список номеров частных автомобилей: ', person_car)
print('Список номеров такси: ', tax_car)
