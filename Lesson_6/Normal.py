# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
import random
import io


class Person:
    def __init__(self, name):
        self._name = name
        print('Generate stats for', self._name)
        with io.open(self._name + '.txt', 'w', encoding='utf-8') as out:
            for key, val in self._generate_stats().items():
                out.write('{}:{}\n'.format(key, val))

    def _generate_stats(self):
        dictionary = {'name': self._name,
                      'health': random.randint(100, 125),
                      'damage': random.randint(20, 30),
                      'armor': 1.2}
        return dictionary

    def _damage(self, dam, heal, defence):
        heal = heal - (dam / defence)
        return round(heal)


class Player(Person):
    def get_stats(self):
        global player
        player = {}
        with open(self._name + '.txt', encoding="utf8") as file:
            for line in file.readlines():
                key, val = line.strip().split(':')
                player[key] = val
        return player

    def _attack(self):
        enemy['health'] = self._damage(int(player['damage']), int(enemy['health']), float(enemy['armor']))
        return enemy['health']


class Enemy(Person):
    def get_stats(self):
        global enemy
        enemy = {}
        with open(self._name + '.txt', encoding="utf8") as file:
            for line in file.readlines():
                key, val = line.strip().split(':')
                enemy[key] = val
        return enemy

    def _attack(self):
        player['health'] = self._damage(int(enemy['damage']), int(player['health']), float(player['armor']))
        return player['health']


class Battle:
    def __init__(self, person1, person2):
        self._person1 = person1
        self._person2 = person2
        print('Победитель:')
        if min(int(player['health']), int(enemy['health'])) > 0:
            while True:
                enemy['health'] = player1._attack()
                if enemy['health'] > 0:
                    player['health'] = player2._attack()
                    if player['health'] <= 0:
                        print(enemy)
                        break
                else:
                    print(player)
                    break


name1 = input('Введите имя первого игрока:')
player1 = Player(name1)
name2 = input('Введите имя второго игрока:')
player2 = Enemy(name2)
Battle(player1.get_stats(), player2.get_stats())
