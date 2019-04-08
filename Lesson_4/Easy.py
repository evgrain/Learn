# Task 1
import copy
import random
list_1 = [random.randint(-10, 10) for i in range(10)]
print('Исходный список:', list_1)
list_2 = copy.deepcopy(list_1)
list_2 = [pow(list_2[value], 2) for value in range(len(list_2))]
print('Изменённый список:', list_2, '\n')

# Task 2
list_1 = ["apple", "banana", "watermelon", "coconut", "grapefruit", "mango"]
list_2 = ["apple", "avocado", "watermelon", "cherimoya", "clementine", "mango"]
result = set(list_1) & set(list_2)
print(list(result), '\n')

# Task 3


def work(list_to_change):
    result = []
    for value in range(len(list_to_change)):
        if list_to_change[value] % 3 == 0 and list_to_change[value] > 3 and list_to_change[value] % 4 != 0:
            result.append(list_to_change[value])
    return result


list_1 = [random.randint(-10, 10) for i in range(10)]
print('Исходный список:', list_1)
print('Изменённый список:', work(list_1))
