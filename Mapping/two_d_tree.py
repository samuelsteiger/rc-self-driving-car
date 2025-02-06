from node import Node
from shapely import Polygon
from random import uniform

class TwoDTree():
    def __init__(self, margin = 0.1):
        self.root = None
        self.margin = margin

    def __str__(self):
        if self.root:
            return self.root.draw_tree()
        else:
            return ""

    def __eq__(self, value):
        queue = []
        #Test for empty trees
        if not self.root:
            if value.root:
                return False
            else:
                return True
        if not value.root:
            return False
        queue.append(self.root)
        while len(queue) > 0:
            current_node = queue.pop()
            if not value.exists(current_node.point.x, current_node.point.y):
                return False
            if current_node.greater:
                queue.append(current_node.greater)
            if current_node.lesser:
                queue.append(current_node.lesser)
        return True

    def insert(self, x, y): 
        node = Node(x,y)
        if not self.root:
            self.root = node
            return
        
        current_node = self.root
        depth = 0
        while True:
            if node.is_greater_than_equal(current_node, depth):
                if current_node.greater:
                    current_node = current_node.greater
                else:
                    current_node.greater = node
                    break
            else:
                if current_node.lesser:
                    current_node = current_node.lesser
                else:
                    current_node.lesser = node
                    break
            depth += 1

    def remove(self, x, y):
        #Find the target node
        if not self.root:
            return
        current_node = self.root
        previous_node = self.root
        target_node = Node(x,y)
        if self.root == target_node and not (self.root.greater or self.root.lesser):
            self.root = None
        depth = 0
        while current_node != target_node:
            if target_node.is_greater_than_equal(current_node, depth):
                if current_node.greater:
                    previous_node = current_node
                    current_node = current_node.greater
                else:
                    return
            else:
                if current_node.lesser:
                    previous_node = current_node
                    current_node = current_node.lesser
                else:
                    return
            depth += 1
        depth -= 1
        #Remove target node
        while current_node.greater or current_node.lesser:
            if current_node.greater:
                current_node.swap(current_node.greater)
                previous_node = current_node
                current_node = current_node.greater
            else:
                current_node.swap(current_node.lesser)
                previous_node = current_node
                current_node = current_node.lesser
        if previous_node.greater:
            previous_node.greater = None
        else:
            previous_node.lesser = None


    def exists(self, x, y):
        current_node = self.root
        target_node = Node(x,y)
        depth = 0
        while current_node != target_node:
            if target_node.is_greater_than_equal(current_node, depth):
                if current_node.greater:
                    current_node = current_node.greater
                else:
                    return False
            else:
                if current_node.lesser:
                    current_node = current_node.lesser
                else:
                    return False
            depth += 1
        return True

    def exists_in_area(self, points):
        queue = [(self.root, 0)]
        area = Polygon(points)

        while len(queue) > 0:
            current_node, depth = queue.pop(0)
            has_greater_equal = False
            has_lesser = False

            for point in points:
                node = Node(point.x, point.y)
                if current_node.is_greater_than_equal(node, depth):
                    has_greater_equal = True
                else:
                    has_lesser = True
            
            #Current node is wholly greater/equal or lesser than the rectangle
            if has_greater_equal ^ has_lesser:
                if has_greater_equal and current_node.greater:
                    queue.append((current_node.greater, depth+1))
                elif has_lesser and current_node.lesser:
                    queue.append((current_node.greater, depth+1))
            #Current node is greater/equal to some corners and less than some corners (or just equal)
            if has_greater_equal or (has_greater_equal and has_lesser):
                if area.contains(current_node.point) or area.intersects(current_node.point):
                    return True
                if current_node.greater:
                    queue.append((current_node.greater, depth+1))
                if current_node.lesser:
                    queue.append((current_node.greater, depth+1))

        return False

    def random_fill(self, count, min = -10, max = 10):
        for i in range(count):
            self.insert(round(uniform(min,max),4), round(uniform(min,max),4))
    