# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа

# in
# 54

# out
# [2, 3, 3, 3]

# in
# 9990

# out
# [2, 3, 3, 3, 5, 37]

# in
# 650

# out
# [2, 5, 5, 13]
def check_number():
    try:
        num = int(input('Enter your number N: '))
        if num < 0:
            return abs(num)
    except ValueError:
        print('Try again.')
        check_number()
    return num

def prime_numbers(num):
    numbers = []
    d = 2
    while d * d <= num:
        if num % d == 0:
            numbers.append(d)
            num //= d
        else:
            d += 1
    if num > 1:
        numbers.append(num)
    return numbers

def Main():
    digit = check_number()
    print('Out: ')
    print(prime_numbers(digit))

Main()

