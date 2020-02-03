'''
bison.py
Maanya Goenka and Katy Oda
October 27, 2018
'''
import time
from random import *
from graphics import *

class Bison:
    def __init__(self, left, top, dark_brown, light_brown):
        self.left=left
        upper_left = Point(left, top)
        self.chest = Oval(upper_left, Point(left + 75, top + 125))
        self.chest.setFill(light_brown)
        self.chest.setOutline(light_brown)
        self.body = Oval(Point(left + 25, top + 25), Point(left + 150, top + 115))
        self.body.setFill(dark_brown)
        self.body.setOutline(dark_brown)
        self.back = Polygon(Point(left + 60, top + 15),
                          Point(left + 100, top + 27),
                          Point(left + 50, top + 60))
        self.back.setFill(light_brown)
        self.back.setOutline(light_brown)
        self.head = Oval(Point(left + 10, top + 25), Point(left - 40, top + 125))
        self.head.setFill(light_brown)
        self.head.setOutline(light_brown)
        self.front_leg = Oval(Point(left + 20, top + 90), Point(left + 50, top + 150))
        self.front_leg.setFill(light_brown)
        self.front_leg.setOutline(light_brown)
        self.back_leg = Oval(Point(left + 100, top + 90), Point(left + 130, top + 150))
        self.back_leg.setFill(dark_brown)
        self.back_leg.setOutline(dark_brown)
        self.tail = Polygon(Point(left + 145, top + 80),
                          Point(left + 160, top + 120),
                          Point(left + 155, top + 125),
                          Point(left + 135, top + 85))
        self.tail.setFill(dark_brown)
        self.tail.setOutline(dark_brown)
        self.tail_tip = Polygon(Point(left + 160, top + 120),
                          Point(left + 162, top + 129),
                          Point(left + 155, top + 125))
        self.tail_tip.setFill(light_brown)
        self.tail_tip.setOutline(light_brown)
        self.horn = Polygon(Point(left - 10, top + 50),
                          Point(left - 20, top + 50),
                          Point(left - 25, top + 5))
        self.horn.setFill(color_rgb(255, 255, 255))
        self.horn.setOutline(color_rgb(255, 255, 255))
        self.front_hoof = Polygon(Point(left + 30, top + 140),
                          Point(left + 40, top + 160),
                          Point(left + 20, top + 160))
        self.front_hoof.setFill(color_rgb(0, 0, 0))
        self.front_hoof.setOutline(color_rgb(0, 0, 0))
        self.back_hoof = Polygon(Point(left + 115, top + 140),
                          Point(left + 125, top + 160),
                          Point(left + 105, top + 160))
        self.back_hoof.setFill(color_rgb(0, 0, 0))
        self.back_hoof.setOutline(color_rgb(0, 0, 0))
        self.eye = Circle((Point(left - 25, top + 65)), 5)
        self.eye.setFill(color_rgb(0, 0, 0))
        self.eye.setOutline(color_rgb(0, 0, 0))


    def draw(self, window):
        self.body.draw(window)
        self.chest.draw(window)
        self.head.draw(window)
        self.eye.draw(window)
        self.front_hoof.draw(window)
        self.front_leg.draw(window)
        self.back_hoof.draw(window)
        self.back_leg.draw(window)
        self.back.draw(window)
        self.tail.draw(window)
        self.tail_tip.draw(window)
        self.horn.draw(window)

    def step(self):
        dx=-4                                
        self.left-=-dx
        if self.left<=0:
            self.left = 804
            self.body.move(804, 0)
            self.chest.move(804, 0)
            self.head.move(804, 0)
            self.eye.move(804, 0)
            self.front_hoof.move(804, 0)
            self.front_leg.move(804, 0)
            self.back_hoof.move(804, 0)
            self.back_leg.move(804, 0)
            self.back.move(804, 0)
            self.tail.move(804, 0)
            self.tail_tip.move(804, 0)
            self.horn.move(804, 0)
        else:
            self.body.move(dx, 0)
            self.chest.move(dx, 0)
            self.head.move(dx, 0)
            self.eye.move(dx, 0)
            self.front_hoof.move(dx, 0)
            self.front_leg.move(dx, 0)
            self.back_hoof.move(dx, 0)
            self.back_leg.move(dx, 0)
            self.back.move(dx, 0)
            self.tail.move(dx, 0)
            self.tail_tip.move(dx, 0)
            self.horn.move(dx, 0)
        pass
