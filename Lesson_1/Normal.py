# Task 1
while True:
    number = int(input('Enter number more then 0 but less then 10\n'))
    if number > 0 and number < 10:
        number **= 2
        print(number, '\n')
        break
    elif number >= 10:
        print('Number ', number, ' is equal or more then 10, you need to type number less then 10 but above 0')
    else:
        print('Number ', number, ' is equal or less then 0, you need to type number above 0 but less then 10')

# Task 2
number1 = int(input('Enter first number\n'))
number2 = int(input('Enter second number\n'))
number1 += number2
number2 = number1 - number2
number1 -= number2
print(number1, number2)
