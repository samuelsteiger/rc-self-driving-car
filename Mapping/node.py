from shapely import Point

class Node():  # Just an example of a base class
    def __init__(self, x, y, greater = None, lesser = None):
        self.point = Point(x, y)
        self.greater = greater
        self.lesser = lesser

    def get_x(self):
        return self.point.x
    
    def get_y(self):
        return self.point.y

    def set_child(self, node, is_greater = True):
        if is_greater:
            self.greater = node
        else:
            self.lesser = node

    def __str__(self):
        return f"({self.point.x},{self.point.y})"
    
    def __repr__(self):
        return f"NODE({self.point.x},{self.point.y})"
    
    def __eq__(self, value):
        if not isinstance(self, Node):
            return False
        if self.point.x != value.point.x:
            return False
        if self.point.y != value.point.y:
            return False
        return True
    
    def swap(self, other):
        temp = self.point
        self.point = other.point
        other.point = temp

    def draw_tree(self, depth = 0):
        root = f"({self.point.x},{self.point.y})"
        left = ""
        right = ""
        if self.greater:
            left = f"\n{(depth + 1) * '-'}g{self.greater.draw_tree(depth + 1)}"
        if self.lesser:
            right = f"\n{(depth + 1) * '-'}l{self.lesser.draw_tree(depth + 1)}"
        return root + left + right
    
    def is_less_than(self, node, depth):
        if depth % 2 == 0:
            return self.point.x < node.point.x
        else:
            return self.point.y < node.point.y
        
    def is_greater_than_equal(self, node, depth):
        if depth % 2 == 0:
            return self.point.x >= node.point.x
        else:
            return self.point.y >= node.point.y
    