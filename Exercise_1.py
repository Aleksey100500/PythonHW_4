# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001

# out
# 8.988
from decimal import Decimal, ROUND_FLOOR

def first_number():
    number = Decimal(input('Enter a real number: '))
    return number

def second_number():
    zero_number = Decimal(input('Enter the required accuracy "0.0001": '))
    return zero_number

def new_number(number, zero_number):
    print('Out: ')
    print(number.quantize(Decimal(zero_number)))

def Main():
    digit_one = first_number()
    digit_two = second_number()
    new_number(digit_one, digit_two)
Main()