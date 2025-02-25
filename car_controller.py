import signal
import sys
import time
from shapely import Point
from Mapping.map import Map 
from Navigation.navigation import Navigation, NavigationMode
from Navigation.directions import Steering, Motor

#How long one cycle of the control flow should take
INTERVAL = 0.1
GOAL_X = -8
GOAL_Y = -8

def sigint_handler(sig, frame):
    #Clean up
    print("Gracefully Terminating")
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

#Setup Controller
key_press = None

map = Map(car_x=-4, car_y=4, car_heading=180)

def decimal_range(min, max):
    return [p/10 for p in range(min * 10, max * 10)]

def draw_line(map:Map, static_coor, start, end, horizontal = True):
    if horizontal:
        for i in decimal_range(start, end):
            map.insert(i, static_coor)
    else:
        for i in decimal_range(start, end):
            map.insert(static_coor, i)

for i in decimal_range(-10, 10):
    #Top Boundary
    map.insert(i, 10)
    #Bottom Boundary
    map.insert(i, -10)
    #Left Boundary
    map.insert(-10, i)
    #Right Boundary
    map.insert(10, i)

    #Individual Lines
draw_line(map, -6, -10, -2, horizontal=False)
draw_line(map, 2, -10, -2, horizontal=False)
draw_line(map, -2, -2, 6, horizontal= False)
draw_line(map, -6, -2, 2, horizontal=True)
draw_line(map, -6, 6, 10, horizontal=True)
draw_line(map, -2, 2, 6, horizontal=True)
draw_line(map, 2, -10, 6, horizontal=True)
draw_line(map, 6, -6, -2, horizontal=True)
draw_line(map, 2, 6, 10, horizontal=False)
draw_line(map, 6, 6, 10, horizontal=True)

map.plot.point(GOAL_X+0.75, GOAL_Y+0.5, marker='E')

nav = Navigation()
nav.build_nav_mesh(map)

while True:
    start_time = time.time()
    #Take Sensor Input

    #Update position in the map
    

    print(map.print())
    #Determine next movement
    steering, motor  = nav.move(map.car.position, Point(GOAL_X, GOAL_Y))
    #Execute Movement
    map.move_car(steering, motor)

    end_time = time.time()
    #Find duration of this cycle in seconds
    elapsed_time = end_time - start_time
    time.sleep(max(INTERVAL - elapsed_time, 0))


    

def build_map_1(map):
    for i in decimal_range(-10, 10):
        #Top Boundary
        map.insert(i, 10)
        #Bottom Boundary
        map.insert(i, -10)
        #Left Boundary
        map.insert(-10, i)
        #Right Boundary
        map.insert(10, i)

    #Individual Lines
    draw_line(map, -6, -10, -2, horizontal=False)
    draw_line(map, 2, -10, -2, horizontal=False)
    draw_line(map, -2, -2, 6, horizontal= False)
    draw_line(map, -6, -2, 2, horizontal=True)
    draw_line(map, -6, 6, 10, horizontal=True)
    draw_line(map, -2, 2, 6, horizontal=True)
    draw_line(map, 2, -10, 6, horizontal=True)
    draw_line(map, 6, -6, -2, horizontal=True)
    draw_line(map, 2, 6, 10, horizontal=False)
    draw_line(map, 6, 6, 10, horizontal=True)