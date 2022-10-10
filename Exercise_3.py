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
from random import randint
import sys
def check_number():
    try:
        number = int(input('Enter your number: ')) 
        print(f'Your number is {number}')  
        if number < 0:
            sys.exit('Negative value of the number of numbers!')
        return number
    except ValueError:
        print('Try again.')
        return check_number()

        
def first_list(number):
    my_list = []
    for i in range(number):
        my_list.append(randint(0, number))
    print(f'My_list: \n{my_list}')
    return my_list

def new_list(my_list, number):
    uniqui_numbers = []
    result = []
    dublicate = []
    for number in my_list:
        if number in uniqui_numbers:
            dublicate.append(number) # добавляем в список dublicate повторяющиеся больше одного раза элементы(удаляя при этом дубликаты) + элементы не повторяющиеся
            continue
        else:
            uniqui_numbers.append(number)
    
    for i in uniqui_numbers: # перечисляем все объекты в списке uniq
        if i in dublicate:   # если число со списка uniq... есть в списке dublicate, то ничего не делаем...
            continue
        else:
            result.append(i) # если его нет, то добавляем в result
    print("Uniqui_numbers: ")
    print(uniqui_numbers)
    print("Dublicate: ")
    print(dublicate)
    print("Result: ")
    print(result)
        

def Main():
    digit = check_number()
    new_list(first_list(digit), digit)
Main()