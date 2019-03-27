class color:
    Red = '\033[91m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    END = '\033[0m'


print(color.Green + 'This is the medical questionnaire' + color.END)
first_name = input('Enter first name: ')
last_name = input('Enter last name: ')
age = int(input('Enter your age: '))
weight = float(input('Enter your weight: '))
if age <= 30 and weight >= 50 and weight <= 120:
    print(color.Green + 'A patient', first_name, last_name, 'have a good health' + color.END)
elif age > 40 and weight < 50 or weight > 120:
    print(color.Red + 'A patient', first_name, last_name, 'need to conduct a medical examination' + color.END)
elif age > 30 and weight < 50 or weight > 120:
    print(color.Yellow + 'A patient', first_name, last_name, 'need to lead a healthy lifestyle' + color.END)
elif age >= 50 and weight == age:
    while True:
        answer = input('your age equal your weight, is that really so? (yes/no) ')
        if answer == 'yes':
            print('Good for you')
            break
        elif answer == 'no':
            print('Please be honest')
            break
        else:
            print('Enter yes or no')
else:
    print(color.Green + 'A patient', first_name, last_name, 'have a good health' + color.END)
