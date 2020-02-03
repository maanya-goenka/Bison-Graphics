from random import *
from graphics import *

class Mountain:
    def __init__(self, left, top, right, width_of_base, height, color):
        lower_left = Point(left, 800-(800//2))
        lower_right = Point(right, 800-(800//2))
        peak = Point(left+width_of_base//2, (800-800//2)+height)
        self.triangle = Triangle(lower_left, lower_right,peak)
        self.triangle.setFill(color)

    def draw(self, window):
        self.triangle.draw(window)
