from node import Node
from shapely import Point
from random import randint

class TwoDTree():
    def __init__(self, margin = 0.1):
        self.root = None
        self.margin = margin

    def __str__(self):
        if self.root:
            return self.root.draw_tree()
        else:
            return ""

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
        pass

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
                    

    def random_fill(self, count, min = -5, max = 5):
        for i in range(count):
            self.insert(randint(min,max), randint(min,max))
    