from Navigation.tile import Tile
from Navigation.priority_queue import PriorityQueue
from shapely import Point, Polygon
from math import sqrt

class AStar():
    def __init__(self, mesh_width = 20, mesh_height = 20):
        #horizontal count of tiles
        self.mesh_width = mesh_width
        #vertical count of tiles
        self.mesh_height = mesh_height
        self.grid = []
        self.queue = PriorityQueue()
        #declaring grid
        for i in range(mesh_width):
            self. grid.append([None] * mesh_height)

    def build_nav_mesh(self, map):
        origin_x = map.plot.xmin
        x_step_distance = (map.plot.xmax - map.plot.xmin) / self.mesh_width
        origin_y = map.plot.ymax
        y_step_distance = (map.plot.ymax - map.plot.ymin) / self.mesh_height
        for i in range(self.mesh_width):
            for j in range(self.mesh_height):
                center = Point(origin_x + i * x_step_distance + x_step_distance/2, origin_y - (j * y_step_distance + y_step_distance/2))
                area = [
                    Point(origin_x + i * x_step_distance + x_step_distance, origin_y - (j * y_step_distance)),
                    Point(origin_x + i * x_step_distance, origin_y - (j * y_step_distance)),
                    Point(origin_x + i * x_step_distance, origin_y - (j * y_step_distance + y_step_distance)),
                    Point(origin_x + i * x_step_distance + x_step_distance, origin_y - (j * y_step_distance + y_step_distance))
                ]
                self.grid[i][j] = Tile(center, area)
                self.grid[i][j].passible = not map.exists_in_area(area)

    def build_path(self, goal:Point, position:Point):
        #find tile containing position and goal
        goal_tile = self.find_tile_by_tile(goal)
        current_tile = self.find_tile_by_tile(position)
        start_tile = current_tile
        current_x, current_y = self.find_tile_by_coor(position)
        current_tile.cost = 0
        self.queue.enqueue(current_tile, current_tile.cost)
        while goal_tile != current_tile:
            current_tile, priority = self.queue.pop()
            current_x, current_y = self.find_tile_by_coor(current_tile.center)
            #Get Adjacent Tiles
            #Drop visited(closed) and impassible tiles
            adjacent = self.get_adjacent_tiles(current_x, current_y)
            
            for tile in adjacent:
                if not tile or not tile.passible or tile.parent:
                    continue
                #Set parents
                tile.parent = current_tile
                #Calculate Costs of Tiles
                self.set_cost(tile, goal)
                #Add to Tile Queue(priority queue)
                self.queue.enqueue(tile,tile.cost)

            #Add Current tile to closed list (maybe we dont need explicit closed list)
        path = []
        while current_tile != start_tile:
            path.insert(0, current_tile.center)
            current_tile = current_tile.parent

        return path

    def grid_get(self, x, y):
        if x >= len(self.grid) or x < 0 or y >= len(self.grid[x] or y < 0):
            return None
        return self.grid[x][y]
    
    def get_adjacent_tiles(self, x, y):
        adjacent = [
            self.grid_get(x+1, y),
            self.grid_get(x-1, y),
            self.grid_get(x, y+1),
            self.grid_get(x, y-1),
            self.grid_get(x-1, y+1),
            self.grid_get(x+1, y+1),
            self.grid_get(x-1, y-1),
            self.grid_get(x+1, y-1)
        ]
        return adjacent
    
    def set_cost(self, current_tile, goal):
        #calculate g (cost from start)
        gx = current_tile.parent.center.x - current_tile.center.x
        gy = current_tile.parent.center.y - current_tile.center.y
        g = sqrt(gx**2 + gy**2)
        #calculate h (cost to goal)
        hx = goal.x - current_tile.center.x
        hy = goal.y - current_tile.center.y
        h = sqrt(hx**2 + hy**2)

        current_tile.cost = current_tile.parent.cost + g + h

        return
    
    def find_tile_by_tile(self, point:Point):
        for tile_row in self.grid:
            for tile in tile_row:
                if Polygon(tile.area).contains(point) or Polygon(tile.area).intersects(point):
                    return tile
                
    def find_tile_by_coor(self, point:Point):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if Polygon(self.grid[i][j].area).contains(point) or Polygon(self.grid[i][j].area).intersects(point):
                    return (i, j)