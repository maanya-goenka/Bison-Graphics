'''prairie.py
Maanya Goenka and Katy Oda
October 29, 2018'''
from graphics import *
from random import *
from mountain import *
from bison import *
def get_random_mountain_color():
    list_of_colors =['olivedrab4','chocolate4','snow4']
    mountain_color_choice = randint(0,2)
    mountain_color=list_of_colors[mountain_color_choice]
    return mountain_color

def get_random_mountain(window_width, window_height):
    color = get_random_mountain_color()
    height_of_greenspace = window_height // 3
    width_of_base = randint(250, window_width //3 )
    height = randint((window_height - height_of_greenspace) // 2, window_height - height_of_greenspace - 15)
    left = randint(0, window_width-20)
    right = left + width_of_base
    mountain = Mountain(left, right, width_of_base, height, color)
    return mountain

def get_bison_colors():
    dark_brown = color_rgb(139, 69, 19)
    light_brown = color_rgb(160, 82, 45)
    return dark_brown, light_brown

def get_random_bison(window_width, window_height):
    height_of_greenspace = window_height // 3
    left = randint(30, window_width - 10)
    width = min(window_width // 25, height_of_greenspace // 3)
    height = width / 1.62
    top = window_height - height_of_greenspace + height
    dark_brown, light_brown = get_bison_colors()
    bison = Bison(left, top, dark_brown, light_brown)
    return bison

def main():
    window_width = 800
    window_height = 800
    window = GraphWin('Prairie', window_width, window_height)
    window.setBackground('cornflower blue')
    greenspace = Rectangle(Point(0,window_height*(2/3)),Point(window_width,800))
    greenspace.setFill('forest green')
    greenspace.draw(window)
    sun = Circle(Point(0, 0),70)
    sun.setFill('DarkGoldenrod1')
    sun.setOutline('goldenrod')
    sun.draw(window)
    for k in range(50):
        mountain = get_random_mountain(window_width, window_height)
        mountain.draw(window)
    print('Type Ctrl-C in the terminal window to make the animation stop.')
    bison = []
    number_of_bison=randint(3,6)
    for k in range(number_of_bison):
        b = get_random_bison(window_width, window_height)
        b.draw(window)
        bison.append(b)
    while True:
        for animal in bison:
            animal.step()
main()
