from Navigation.directions import Steering, Motor
from Navigation.a_star import AStar
import random
from enum import Enum
from math import atan2, degrees
from shapely import Polygon

class NavigationMode(Enum):
    RANDOM = 1
    A_STAR = 2

class Navigation():
    def __init__(self):
        self.path = None
        self.pathfinder = AStar(mesh_width=10, mesh_height=10)
        self.map = None
        self.next_position = None

    def move(self, start = None, end = None):
        if not self.path:
            self.path = self.pathfinder.build_path(end, start)
        if len(self.path) <= 0:
            return self.random_move()
        if self.next_position and (Polygon(self.map.car.get_car_area()).contains(self.next_position) or Polygon(self.map.car.get_car_area()).intersects(self.next_position)):
            self.next_position = None
        if not self.next_position:
            self.next_position = self.path.pop(0)
        

        return (self.steer(self.next_position), Motor.FORWARD)

    def build_nav_mesh(self, map):
        self.map = map
        self.pathfinder.build_nav_mesh(map)

    def random_move():
        rand_steering  = random.randint(1,3)
        rand_motor  = random.randint(1,3)

        move = [None, None]

        if rand_steering == 1:
            move[0] = Steering.COUTNER_CLOCKWISE
        if rand_steering == 2:
            move[0] = Steering.CLOCKWISE
        if rand_motor == 1:
            move[1] = Motor.FORWARD
        if rand_motor == 2:
            move[1] = Motor.BACKWARD
        
        move = (move[0], move[1])

        return move

    def steer(self, position):
        x = position.x - self.map.car.position.x
        y = position.y - self.map.car.position.y
        target_heading = degrees(atan2(y, x))
        if(target_heading < 0):
            target_heading += 360
        if(target_heading > 360):
            target_heading -= 360

        ##self.map.car.heading = target_heading

        if abs(target_heading - self.map.car.heading) < 30:
            return None
        elif (target_heading > self.map.car.heading and target_heading < self.map.car.heading + 180) or (target_heading <= self.map.car.heading - 180):
            return Steering.COUTNER_CLOCKWISE
        else:
            return Steering.CLOCKWISE