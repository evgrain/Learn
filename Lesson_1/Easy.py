from datetime import datetime, date, time
# Task 1
greetings = 'Hello, today is'
print(greetings, datetime.now())
name = input('What is your name?\n')
name += ','
work_date = date(2019, 3, 26)
print('Nice to meet you', name, 'I\'ve made this programm at', work_date)

# Task 2
number = int(input('Enter number: '));
print(number, '+ 2 =', number + 2)

# Task 3
age = int(input('How old are you?\n'))
if age >= 18:
    print(name, 'access granted')
else:
    print(name, 'you must be above 18 to continue')
