import signal
import sys
import time
from shapely import Point
from Mapping.map import Map 
from Navigation.navigation import Navigation, NavigationMode
from Navigation.directions import Steering, Motor

#How long one cycle of the control flow should take
INTERVAL = 0.1

def sigint_handler(sig, frame):
    #Clean up
    print("Gracefully Terminating")
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

#Setup Controller
key_press = None

map = Map()


for i in range(-9, 9, 1):
    map.insert(i, 9)
    map.insert(i, -9)
    map.insert(9, i)
    map.insert(-9, i)

for i in range(-9, 6, 1):
    map.insert(i, 3)

for i in range(9, -6, -1):
    map.insert(i, -3)

nav = Navigation()
nav.build_nav_mesh(map)

while True:
    start_time = time.time()
    #Take Sensor Input

    #Update position in the map
    

    print(map.print())
    #Determine next movement
    steering, motor  = nav.move(map.car.position, Point(7, -7))
    #Execute Movement
    map.move_car(steering, motor)

    end_time = time.time()
    #Find duration of this cycle in seconds
    elapsed_time = end_time - start_time
    time.sleep(max(INTERVAL - elapsed_time, 0))

