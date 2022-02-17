class Road:
    _length = None
    _width = None

    def __init__(self, _length, _width):
        self._length = _length
        self._width =_width

    def mass_(self):
        self.weigth = 25
        self.tickness = 1.25
        intake = self._length * self._width * self.weigth * self.tickness / 1000
        print(f'необходимо {intake} тонн для строительства дороги')

road_to_village = Road(50000, 6)
road_to_village.mass_()