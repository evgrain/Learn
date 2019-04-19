import random


class Loto:
    def __init__(self):
        self._numbers = self._root()
        self.card = [self._generate(self._numbers), self._generate(self._numbers), self._generate(self._numbers)]

    def _root(self):
        return [number for number in range(1, 91)]

    def _add_numbers(self, count, score):
        if count <= 5 and score < 5:
            return True
        elif count <= 5 and score >= 5:
            return False
        else:
            return random.choice([True, False])

    def random_number(self, number, array):
        max = number * 10
        while True:
            result = random.randint(number, max)
            print(result)
            if result in array:
                return result

    def _generate(self, all_numbers):
        card = []
        count = 9
        score = 0
        for number in range(1, 10):
            while True:
                if self._add_numbers(count, score) is True:
                    rand = self.random_number(number, all_numbers)
                    card.append(rand)
                    all_numbers.remove(rand)
                    score += 1
                    break
                else:
                    card.append('')
                    break
            count -= 1
        return card

    def show_card(self):
        string = ''
        for line in self.card:
            for element in line:
                string = string + str(element) + '  '
            string += '\n'
        print(string[:-1])

    def end(self, array):
        numbers = 0
        for line in array:
            for value in line:
                try:
                    value = str(value)
                    if value.isdigit() is True:
                        numbers += 1
                except AttributeError:
                    pass
        if numbers == 0:
            return False


class Human(Loto):
    def out(self):
        print('------ Ваша карточка -----')
        self.show_card()
        print('-'*26)

    def search(self, number, array):
        for source in array:
            if number in source:
                return True
        return False

    def remove(self, number):
        if self.search(number, self.card):
            for line in self.card:
                if number in line:
                    line.insert(line.index(number), '-')
                    line.pop(line.index(number))
            return True
        else:
            print('Такого числа у вас нет, игра окончена')
            return False


class Computer(Loto):

    def out(self):
        print('-- Карточка компьютера ---')
        self.show_card()
        print('-' * 26)

    def remove(self, number):
        for line in self.card:
            if number in line:
                line.insert(line.index(number), '-')
                line.pop(line.index(number))


class Game:
    def __init__(self, human, computer):
        self.barrels = Loto._root(self)
        self.game = True
        while True:
            self.test = self.barrel(self.barrels)
            if self.game is False:
                break
            elif human.end(human.card) is False:
                print('Победил человек')
                break
            elif computer.end(computer.card) is False:
                print('Победил компьютер')
                break
            print('\n' * 20)
            print('Новый бочонок с номером', self.test[0], 'осталось', self.test[1], 'бочёнков')
            while True:
                human.out()
                computer.out()
                answer = input('Зачеркнуть цифру? (y/n)')
                computer.remove(self.test[0])
                if answer == 'y':
                    self.game = human.remove(self.test[0])
                    break
                elif answer == 'n':
                    if human.search(self.test[0], human.card) is True:
                        print('У вас в карточке было число', self.test[0], 'игра окончена')
                        self.game = False
                    break
                else:
                    print('Вы ввели не \'y\' и не \'n\', игра окончена')
                    self.game = False
                    break

    def barrel(self, barrels):
        result = []
        rand = random.choice(barrels)
        result.append(rand)
        barrels.remove(rand)
        result.append(len(barrels))
        return result


start = Game(Human(), Computer())
