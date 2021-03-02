import math


class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, x, y):
        first_num = abs(self.x - x)
        second_num = self.y - y
        nums = math.sqrt((first_num * first_num) + (second_num * second_num))
        return nums


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))
