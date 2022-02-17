class Cars:
    is_police = None

    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return "The car went"

    def stop(self):
        return "The car has stopped"

    def turn(self, direction):
        return "The car turned to "  + direction

class TownCar(Cars):
        family = None

        def __init__(self, name, speed, color, family = True):
            super().__init__(name, speed, color)
            self.family = family

class SportCar(Cars):
        def __init__(self, name, speed, color):
            super().__init__(name, speed, color)

class WorkCar(Cars):
        def __init__(self, name, speed, color, is_police):
            super().__init__(name, speed, color, is_police)

class PoliceCar(Cars):
        def __init__(self, name, speed, color):
            super().__init__(name, speed, color, True)

ford = TownCar('Ford', 60, 'black')
print(ford.name, ford.color, ford.speed, ford.is_police)
print(ford.go(), ford.turn('City'), ford.stop())
sport = SportCar('Porsche', 320, 'red')
work1 = WorkCar('Mazda', 120, 'white', True)
work2 = WorkCar('Audi', 90, 'white', False)
police = PoliceCar('Ford', 180, 'red')