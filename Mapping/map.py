from Mapping.two_d_tree import TwoDTree
from Mapping.car import Car
import plotille
import time
import random
from shapely import Point
from Navigation.directions import Steering, Motor
from copy import deepcopy
import os 

WIDTH, HEIGHT = os.get_terminal_size()

class Map():
    def __init__(self, car_x = 0, car_y = 0, car_heading = 0):
        self.plot = plotille.Canvas(width= WIDTH,
                      height= HEIGHT - 1,
                       xmin=-10,
                        ymin=-10,
                         xmax=10,
                          ymax=10)
        self.tree = TwoDTree()
        self.car = Car(x = car_x, y = car_y, heading = car_heading)
        self.add_car()

    def insert(self, x, y):
        self.tree.insert(x, y)
        self.plot.point(x,y)

    def remove(self, x, y):
        self.tree.remove(x, y)
        self.plot.point(x,y,set_=False)

    def exists(self, x, y):
        return self.tree.exists(x, y)

    def exists_in_area(self, points):
        return self.tree.exists_in_area(points)
    
    def get_map_area(self):
        return (self.plot.xmin, self.plot.xmax, self.plot.ymin, self.plot.ymax)

    def print(self):
        print("\033c")
        print(self.plot.plot())

    def random_plot(self):
        while True:
            self.insert(round(random.uniform(-10,10),4), round(random.uniform(-10,10),4))
            print("\033c")
            print(self.plot.plot())
            time.sleep(0.1)

    def remove_car(self):
        rect = self.car.get_car_area()
        self.plot.line(rect[0].x, rect[0].y, rect[1].x, rect[1].y, set_= False)
        self.plot.line(rect[1].x, rect[1].y, rect[2].x, rect[2].y, set_= False)
        self.plot.line(rect[2].x, rect[2].y, rect[3].x, rect[3].y, set_= False)
        self.plot.line(rect[3].x, rect[3].y, rect[0].x, rect[0].y, set_= False)

    def add_car(self):
        rect = self.car.get_car_area()
        self.plot.line(rect[0].x, rect[0].y, rect[1].x, rect[1].y)
        self.plot.line(rect[1].x, rect[1].y, rect[2].x, rect[2].y)
        self.plot.line(rect[2].x, rect[2].y, rect[3].x, rect[3].y)
        self.plot.line(rect[3].x, rect[3].y, rect[0].x, rect[0].y)

    def move_car(self, steering, motor):
        self.remove_car()
        old_car = deepcopy(self.car)

        if steering == Steering.COUTNER_CLOCKWISE:
            self.car.turn_left()
        if steering == Steering.CLOCKWISE:
            self.car.turn_right()
        if motor == Motor.FORWARD:
            self.car.move_forwards()
        if motor == Motor.BACKWARD:
            self.car.move_backwards()

        #Check if new position is valid
        if not self.is_valid_movement():
            self.car = old_car

        self.add_car()

    def is_valid_movement(self):
        return not self.tree.exists_in_area(self.car.get_car_area())