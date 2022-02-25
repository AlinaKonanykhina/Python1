class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'All right'
                else:
                    return f'ОШИБКА Неправильный год'
            else:
                return f'ОШИБКА Неправильный месяц'
        else:
            return f'ОШИБКА Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('20 - 2 - 2022')
print(today)
print(Data.valid(11, 11, 2023))
print(today.valid(11, 14, 2022))
print(Data.extract('11 - 1 - 2022'))
print(today.extract('11 - 1 - 2022'))
print(Data.valid(25, 2, 2022))