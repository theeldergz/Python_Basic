import re

numbers_list = ['9999999999', '999999-999', '99999x9999', '88005553435', '6999999999']

pattern = r'\b[89]\d{9}'

for number in numbers_list:
    if re.match(pattern, number):
        print(number, 'подходит')
    else:
        print(number, 'не подходит')

