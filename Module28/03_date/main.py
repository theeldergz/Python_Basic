from typing import List


class Date:
    """ Класс отвечающий за работу с датами """

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'День: {self.day}	Месяц: {self.month}	Год: {self.year}'

    @classmethod
    def __formatted_date(cls, input_date: str) -> List[int]:
        """ Метод, приводит введенную строкой дату, в список дат приведенных к int  """
        formatted_date: list = input_date.split('-')
        formatted_date: list[int] = [int(value) for value in formatted_date]
        return formatted_date

    @classmethod
    def from_string(cls, input_date: str) -> 'Date':
        """ Метод, возвращает строку приведенную к формату вида  День:  Месяц:  Год:   """
        day, month, year = cls.__formatted_date(input_date)
        date_obj = cls(day, month, year)
        return date_obj

    @classmethod
    def is_date_valid(cls, input_date: str) -> bool:
        """ Метод, проверяет строку на соответствие с реальным датами dd-mm-yyyy """
        form_date: list[int] = Date.__formatted_date(input_date)
        if 1 <= form_date[0] <= 31 and 1 <= form_date[1] <= 12 and form_date[2] > 0:
            return True
        return False


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
