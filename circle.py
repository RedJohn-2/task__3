import math

from point import Point


class Circle:
    def __init__(self, mid_point: Point, r: float):
        self.mid_point = mid_point
        self.r = r

    def is_inner_circle(self, outer_circle: __init__):
        return outer_circle.r >= self.r + self.mid_point.to_point(outer_circle.mid_point)

    def calc_perimeter(self):
        return 2 * math.pi * self.r
