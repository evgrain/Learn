# Task 1
fruits = ["apple", "banana", "watermelon", "coconut", "grapefruit", "mango"]
count = 1
for index in fruits:
    print(count, '{:>10}'.format(index))
    count += 1

# Task 2
list_1 = {"apple", "banana", "watermelon", "coconut", "grapefruit", "mango"}
list_2 = {"apple", "avocado", "watermelon", "cherimoya", "clementine", "mango"}
list_1 -= list_2
print(list_1)

# Task 3
numbers = [10, 2, 5, 6, 42, 7]
new_numbers = []
for number in numbers:
    if number % 2 == 0:
        new_numbers.append(number / 4)
    else:
        new_numbers.append(number * 2)
print(new_numbers)
