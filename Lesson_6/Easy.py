class TemplateCar:
    def __init__(self, name, color, speed):
        self.speed = speed
        self.color = color
        self.name = name
        self._initialization()

    def _initialization(self):
        print('{color} - {name} - max speed {speed} km\h'.format(name=self.name, color=self.color, speed=self.speed))

    def go(self):
        print('Car is moving')

    def stop(self):
        print('Car is stopped')

    def turn(self, direction):
        if direction is 'left' or direction is 'right' or direction is 'back':
            print('Car is turning', direction)
        else:
            print('Can\'t turn that way')


class TownCar(TemplateCar):
    def __init__(self, name, color, speed):
        print('=== This is town car ===')
        super().__init__(name, color, speed)
        print('=' * 25)

    def unexpected_drift(self):
        print('Car is drifting')


class SportCar(TemplateCar):
    def __init__(self, name, color, speed):
        print('=== This is sport car ===')
        super().__init__(name, color, speed)
        print('=' * 25)

    def go_fast(self):
        print('Move with the high speed')


class WorkCar(TemplateCar):
    def __init__(self, name, color, speed):
        print('=== This is work car ===')
        super().__init__(name, color, speed)
        print('=' * 25)


class PoliceCar(TemplateCar):
    def __init__(self, name, color, speed):
        print('=== This is police car ===')
        super().__init__(name, color, speed)
        self._is_police = True
        print('=' * 25)

    def call(self):
        print('Police is on the way')


def handling(list_of_cars):
    for dicts in list_of_cars:
        for key, value in dicts.items():
            if key is 'Name' and value is 'Hundai':
                temp_list = list(dicts.values())
                global town_car
                town_car = TownCar(temp_list[0], temp_list[1], temp_list[2])
            if key is 'Speed' and value > 180:
                temp_list = list(dicts.values())
                global sport_car
                sport_car = SportCar(temp_list[0], temp_list[1], temp_list[2])
            if key is 'Name' and value is 'BMW':
                temp_list = list(dicts.values())
                global work_car
                work_car = WorkCar(temp_list[0], temp_list[1], temp_list[2])
            if key is 'Police' and value is True:
                temp_list = list(dicts.values())
                global police_car
                police_car = PoliceCar(temp_list[0], temp_list[1], temp_list[2])


list_of_cars = [{'Name': 'Hundai', 'Color': 'Red', 'Speed': 150, 'Police': False},
                {'Name': 'Ferrari', 'Color': 'Yelloow', 'Speed': 220, 'Police': False},
                {'Name': 'BMW', 'Color': 'Black', 'Speed': 120, 'Police': False},
                {'Name': 'Ranger', 'Color': 'White-blue', 'Speed': 160, 'Police': True}]
handling(list_of_cars)
print('\n\n')
sport_car.go_fast()
town_car.turn('left')
town_car.unexpected_drift()
police_car.call()
