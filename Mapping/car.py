from shapely import Point, Polygon
import math

LENGTH = 0.5
WIDTH = 0.25
TURN_RADIUS = 60
MOVE_DISTANCE = 1

class Car():
    def __init__(self, x=0, y=0, heading = 90):
        self.position = Point(x, y)
        self.heading = heading

    def get_car_area():
        pass

    def turn_right(self):
        self.heading = self.heading - TURN_RADIUS
        if self.heading < 0:
            self.heading += 360

    def turn_left(self):
        self.heading = self.heading + TURN_RADIUS
        if self.heading >= 360:
            self.heading -= 360

    def move_forwards(self):
        x = (MOVE_DISTANCE * math.cos(math.radians(self.heading))) + self.position.x
        y = (MOVE_DISTANCE * math.sin(math.radians(self.heading))) + self.position.y
        self.position = Point(x,y)

    def move_backwards(self):
        x = (MOVE_DISTANCE * math.cos(math.radians(self.heading + 180))) + self.position.x
        y = (MOVE_DISTANCE * math.sin(math.radians(self.heading + 180))) + self.position.y
        self.position = Point(x,y)

    def get_car_area(self):
        #The four corners of the cars area
        points = []
        #Front-Right Corner

        #Front-Left Corner

        #Back-Left Corner

        #Back-Right Corner