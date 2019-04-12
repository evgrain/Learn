# Task 1
from Easy import move_to_dir
from Easy import list_dir
from Easy import remove_dir
from Easy import create_dir


while True:
    chose = input('Введите цифру соответствующую нужному действию\n' + '-' * 40 + '\n'
                                                                                  '1. Перейти в папку\n'
                                                                                  '2. Просмотреть содержимое текущей папки\n'
                                                                                  '3. Удалить папку\n'
                                                                                  '4. Создать папку\n' + '-' * 40 + '\n')
    if chose.isnumeric() is True:
        chose = int(chose)
        if chose == 1:
            path = input('В какую директорию хотите перети? ')
            move_to_dir(path)
        elif chose == 2:
            list_dir()
        elif chose == 3:
            path = input('Какую папку удалить? ')
            remove_dir(path)
        if chose == 4:
            path = input('Введите название для папки: ')
            create_dir(path)
    else:
        print('Введите одну цифру\n')
