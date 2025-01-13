from node import Node
from shapely import Point

class TwoDTree():
    def __init__(self, margin = 0.1):
        self.root = None
        self.margin = margin

    def __str__(self):
        if self.root:
            return self.root.__str__()
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
            if current_node.is_less_than(node, depth):
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
        pass
    
tree = TwoDTree()
tree.insert(0,0)
tree.insert(2,3)
tree.insert(-4,-6)
tree.insert(3,-9)
tree.insert(0,0)
print(tree)