# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

# set нельзя использовать
from random import randint
from itertools import groupby

def check_number():
    try:
        number = int(input('Enter your number: '))
        if number < 0:
            print('Negative value of the number of numbers!\n[]')
            return check_number()
    except ValueError:
        print('Try again.')
        check_number()
    return number

def first_list(number):
    my_list = []
    for i in range(number):
        my_list.append(randint(0, number))
    print(my_list)
    return my_list

def new_list(my_list, number):
    uniqui_numbers = []
    for number in my_list:
        if number in uniqui_numbers:
            continue
        else:
            uniqui_numbers.append(number)
    
    print(uniqui_numbers)
        
def Main():
    digit = check_number()
    print(f'Your number: {digit}\n')
    new_list(first_list(digit), digit)

Main()