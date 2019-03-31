# coding: cp1251
# Task 1
print('Task 1')
from math import sqrt, floor
numbers = [10, 0, 2, -5, 36, 6, 42, 7, 8, 4, 49]
new_numbers = []
for number in numbers:
    if number > 0:
        test_number = sqrt(number)
        if floor(test_number * 100) % 10 == 0:
            new_numbers.append(floor(test_number))
print(new_numbers)

# Task 2
print('\nTask 2')
date = '31.03.2019'
int_date = date.split('.')
day = ('превое', 'второе', 'третье', 'четвёртое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое', 'одиннадцатое', 'двенадцатое', 'тренадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое', 'семнадцатое', 'восемьнадцатое', 'девятьнадцатое', 'двадцатое', 'двадцатьпервое', 'двадцатьвторое', 'двадцатьтретье', 'двадцатьчетвёртое', 'двадцатьпятое', 'двадцатьшестое', 'двадцатьседьмое', 'двадцатьвосьмое', 'двадцатьдевятое', 'тридцатое', 'тридцатьпервое')
month = ('января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря')
if int(int_date[0]) > 0 and int(int_date[0]) <= 31 and int(int_date[1]) > 0 and int(int_date[1]) <= 12:
    print(f'{day[int(int_date[0])-1]} {month[int(int_date[1])-1]} {int_date[2]} года')
else:
    print('Неверно указана дата')

# Task 3
print('\nTask 3')
import random
print('Enter number of digits')
digit = random.randint(1, 20)
numbers = []
for _ in range(digit):
    numbers.append(random.randint(-100, 100))
print(numbers)

# Task 4
print('\nTask 4')
numbers_1 = [1, 3, 2, 1, 4, 5, 6, 1, 6, 7, 8, 3, 5, 9, 7, 9]
numbers_2 = []
numbers_3 = []
dict = {}
# part a
numbers_2 = set(numbers_1)
print(numbers_2)
# part b
for i in numbers_1:
  dict[i] = dict.get(i, 0) + 1
for key, value in dict.items():
  if value == 1:
    numbers_3.append(key)
print(numbers_3)
