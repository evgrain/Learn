# Task 1
def life(name, age, city):
    result = name + ', ' + age + ' год(а), проживает в городе ' + city
    return result


name = 'John'
age = '29'
city = 'Ekaterinburg'
result = life(name, age, city)
print(result)


# Task 2
x = 5
y = 7
z = 3
result = (lambda a, b, c: max(a, b, c))(x, y, z)
print(result)


# Task 3
def str_max(*args):
    dict = {}
    index = 1
    max_length = (max(map(len, strings)))
    for string in strings:
        if max_length == len(string):
            dict[index] = string
            index += 1
    dict = list(dict.values())
    return dict


strings = []
while True:
    strings.append(input('Введите строку (для выхода введите stop): '))
    if strings[-1] == 'stop':
        strings.pop(-1)
        break
result = str_max(strings)
print('Самая длинная строка/сктроки ', result)
