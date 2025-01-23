from two_d_tree import TwoDTree
import plotille
import time
import random
from shapely import Point

class Map():
    def __init__(self):
        self.plot = plotille.Canvas(width=60, 
                      height=20,
                       xmin=-10,
                        ymin=-10,
                         xmax=10,
                          ymax=10)
        self.tree = TwoDTree()
        self.car = Point(0,0)

    def insert(self, x, y):
        self.tree.insert(x, y)
        self.plot.point(x,y)

    def remove(self, x, y):
        self.tree.remove(x, y)
        self.plot.point(x,y,set_=False)

    def exists(self, x, y):
        return self.tree.exists(x, y)
    
    def random_plot(self):
        while True:
            self.insert(round(random.uniform(-10,10),4), round(random.uniform(-10,10),4))
            print("\033c")
            print(self.plot.plot())
            time.sleep(0.1)

map = Map()
map.random_plot()