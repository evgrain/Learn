import random
import io


def generate_stats(string):
    dictionary = {'name': string, 'health': random.randint(100, 125), 'damage': random.randint(20, 30), 'armor': 1.2}
    return dictionary


def attack(dam, heal, defence):
    heal = heal - (dam / defence)
    return round(heal)


def action(name1, name2):
    player1 = {}
    player2 = {}
    with open(name1 + '.txt', encoding="utf8") as file1:
        for line in file1.readlines():
            key, val = line.strip().split(':')
            player1[key] = val
    print(player1)
    with open(name2 + '.txt', encoding="utf8") as file2:
        for line in file2.readlines():
            key, val = line.strip().split(':')
            player2[key] = val
    print(player2)
    if min(int(player1['health']), int(player2['health'])) > 0:
        while True:
            player2['health'] = attack(int(player1['damage']), int(player2['health']), float(player2['armor']))
            if player2['health'] > 0:
                player1['health'] = attack(int(player2['damage']), int(player1['health']), float(player1['armor']))
                if player1['health'] <= 0:
                    return player2
            else:
                return player1


name1 = input('Введите имя первого игрока:')
player1 = generate_stats(name1)
with io.open(name1 + '.txt', 'w', encoding='utf-8') as out:
    for key, val in player1.items():
        out.write('{}:{}\n'.format(key, val))
name2 = input('Введите имя второго игрока:')
player2 = generate_stats(name2)
with io.open(name2 + '.txt', 'w', encoding='utf-8') as out:
    for key, val in player2.items():
        out.write('{}:{}\n'.format(key, val))
result = action(name1, name2)
print('Winner is:', result['name'], 'which left', result['health'], 'hitpoint')
