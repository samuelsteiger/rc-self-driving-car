from shapely import Point, Polygon
from math import cos, sin, radians

LENGTH = 5
WIDTH = 2.5
TURN_RADIUS = 3
MOVE_DISTANCE = 1

class Car():
    def __init__(self, x=0, y=0, heading = 134):
        self.position = Point(x, y)
        self.heading = heading

    def turn_right(self):
        self.heading = self.heading - TURN_RADIUS
        if self.heading < 0:
            self.heading += 360

    def turn_left(self):
        self.heading = self.heading + TURN_RADIUS
        if self.heading >= 360:
            self.heading -= 360

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
        x1 = x + (WIDTH/2) * cos(radians(self.heading)) + (LENGTH/2) * sin(radians(self.heading))
        y1 = y + (WIDTH/2) * sin(radians(self.heading)) - (LENGTH/2) * cos(radians(self.heading))
        #Front-Left Corner
        x2 = x + (WIDTH/2) * cos(radians(self.heading)) - (LENGTH/2) * sin(radians(self.heading))
        y2 = y + (WIDTH/2) * sin(radians(self.heading)) + (LENGTH/2) * cos(radians(self.heading))
        #Back-Left Corner
        x3 = x - (WIDTH/2) * cos(radians(self.heading)) - (LENGTH/2) * sin(radians(self.heading))
        y3 = y - (WIDTH/2) * sin(radians(self.heading)) + (LENGTH/2) * cos(radians(self.heading))
        #Back-Right Corner
        x4 = x - (WIDTH/2) * cos(radians(self.heading)) + (LENGTH/2) * sin(radians(self.heading))
        y4 = y - (WIDTH/2) * sin(radians(self.heading)) - (LENGTH/2) * cos(radians(self.heading))
        #The four corners of the cars area
        points = [Point(x1,y1), Point(x2,y2), Point(x3,y3), Point(x4,y4)]
        return points
