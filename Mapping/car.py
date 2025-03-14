from shapely import Point, Polygon
from math import cos, sin, radians

LENGTH = 0.25
WIDTH = 0.25
TURN_RADIUS = 45
MOVE_DISTANCE = 0.2

class Car():
    def __init__(self, x=-7, y=7, heading = 90):
        self.position = Point(x, y)
        self.heading = heading

    def turn_right(self):
        self.heading = self.heading - TURN_RADIUS
        if self.heading >= 360:
            self.heading -= 360
        if self.heading < 0:
            self.heading += 360

    def turn_left(self):
        self.heading = self.heading + TURN_RADIUS
        if self.heading >= 360:
            self.heading -= 360
        if self.heading < 0:
            self.heading += 360

    def set_heading(self, heading):
        self.heading = heading
        if self.heading >= 360:
            self.heading -= 360
        if self.heading < 0:
            self.heading += 360


    def move_forwards(self):
        x = (MOVE_DISTANCE * cos(radians(self.heading))) + self.position.x
        y = (MOVE_DISTANCE * sin(radians(self.heading))) + self.position.y
        self.position = Point(x,y)

    def move_backwards(self):
        x = (MOVE_DISTANCE * cos(radians(self.heading + 180))) + self.position.x
        y = (MOVE_DISTANCE * sin(radians(self.heading + 180))) + self.position.y
        self.position = Point(x,y)

    def get_car_area(self):
        x = self.position.x
        y = self.position.y
        #Front-Right Corner
        x1 = x + (LENGTH/2) * cos(radians(self.heading)) + (WIDTH/2) * sin(radians(self.heading))
        y1 = y + (LENGTH/2) * sin(radians(self.heading)) - (WIDTH/2) * cos(radians(self.heading))
        #Front-Left Corner
        x2 = x + (LENGTH/2) * cos(radians(self.heading)) - (WIDTH/2) * sin(radians(self.heading))
        y2 = y + (LENGTH/2) * sin(radians(self.heading)) + (WIDTH/2) * cos(radians(self.heading))
        #Back-Left Corner
        x3 = x - (LENGTH/2) * cos(radians(self.heading)) - (WIDTH/2) * sin(radians(self.heading))
        y3 = y - (LENGTH/2) * sin(radians(self.heading)) + (WIDTH/2) * cos(radians(self.heading))
        #Back-Right Corner
        x4 = x - (LENGTH/2) * cos(radians(self.heading)) + (WIDTH/2) * sin(radians(self.heading))
        y4 = y - (LENGTH/2) * sin(radians(self.heading)) - (WIDTH/2) * cos(radians(self.heading))
        #The four corners of the cars area
        points = [Point(x1,y1), Point(x2,y2), Point(x3,y3), Point(x4,y4)]
        return points
