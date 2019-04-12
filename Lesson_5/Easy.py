# Task 1
import os


def move_to_dir(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print('Такой папки нет\n')


def list_dir():
    dirs = os.listdir('.')
    for content in dirs:
        print(content)


def remove_dir(path):
    try:
        os.rmdir(path)
    except FileNotFoundError:
        print('Такой папки нет')


def create_dir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        print('Такая папка уже существует\n')


name = ['dir_' + str(count) for count in range(1, 10)]
root_path = '.'
for folder in name:
    create_dir(folder)

# Task 2
for directory in os.listdir('.'):
    if os.path.isdir(directory):
        print(directory)

# Task 3
import shutil

shutil.copyfile(os.path.basename(__file__), os.path.basename(__file__) + '_copy')