class DivisionNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"ОШИБКА Деление на ноль недопустимо")


div = DivisionNull(8, 10)
print(DivisionNull.divide_null(5, 0))
print(DivisionNull.divide_null(100, 0.1))
print(div.divide_null(100, 0))
print(div.divide_null(100, 5))