class Tile():
    def __init__(self, center, area):
        self.center = center
        self.area = area
        self.passible = False
        self.parent = None
        self.cost = None

    def __eq__(self, value):
        if not isinstance(value):
            return False
        return self.center == value.center
