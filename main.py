import math

from circle import Circle
from point import Point


def find_inner_circle(list_circles):
    max_circles = 0
    inner_circle = None
    perimeter = math.inf
    for i in range(0, len(list_circles)):
        count_circles = 0
        for j in range(0, len(list_circles)):
            if i != j:
                if list_circles[i].is_inner_circle(list_circles[j]):
                    count_circles += 1
        if count_circles > max_circles:
            max_circles = count_circles
            inner_circle = list_circles[i]
        elif count_circles == max_circles and list_circles[i].calc_perimeter() < perimeter:
            max_circles = count_circles
            inner_circle = list_circles[i]
            perimeter = list_circles[i].calc_perimeter()

    return inner_circle


def read_from_file(file_name: str):
    f = open(file_name, 'r')
    l = []
    for line in f:
        temp = [float(x) for x in line.strip().split(" ")]
        l.append(Circle(Point(temp[0], temp[1]), temp[2]))
    f.close()
    return l


def write_to_file(circle: Circle, file_name: str):
    circle_to_list = [circle.mid_point.x, circle.mid_point.y, circle.r]
    f = open(file_name, 'w')
    f.write(" ".join([str(x) for x in circle_to_list]))


circles = read_from_file("input2.txt")
write_to_file(find_inner_circle(circles), "output.txt")
