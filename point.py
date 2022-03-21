class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def to_point(self, p: __init__):
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5
