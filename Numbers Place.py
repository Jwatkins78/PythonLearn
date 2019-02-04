from decimal import Decimal

values = [
    ('hundreds',   Decimal(100)),
    ('tens',   Decimal(10)),
    ('fives',  Decimal(5)),
    ('ones',   Decimal(1)),
    ('tenths', Decimal('0.1'))
]

def get_digits(num):
    output_dict = {}
    for place, value in values:
        output_dict[place] = int(num // value)
        num = num % value
    return output_dict

num = Decimal(input("input number: "))
print(get_digits(num))

