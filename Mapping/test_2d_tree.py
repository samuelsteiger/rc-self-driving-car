import unittest
from node import Node
from two_d_tree import TwoDTree
from shapely import Point

class TestTwoDTree(unittest.TestCase):

    def setUp(self):
        pass

    def test_valid_tree(self):
        tree1 = TwoDTree()
        tree1.root = Node(2,4)
        tree1.root.greater = Node(3,-1)
        tree1.root.lesser = Node(-8,0)
        tree1.root.greater.greater = Node(5,1)
        tree1.root.greater.lesser = Node(7,-3)
        tree1.root.lesser.greater = Node(-2, 9)
        tree1.root.lesser.lesser = Node(-5,-7)

        tree2 = TwoDTree()
        tree2.random_fill(10)

        tree3 = TwoDTree()
        tree3.random_fill(1000)
        
        tree4 = TwoDTree()
        tree4.root = Node(2,4)
        tree4.root.greater = Node(3,-1)
        tree4.root.lesser = Node(-8,0)
        tree4.root.greater.greater = Node(5,-2)
        tree4.root.greater.lesser = Node(7,-3)
        tree4.root.lesser.greater = Node(-2, 9)
        tree4.root.lesser.lesser = Node(-5,-7)

        self.assertTrue(is_valid_tree(tree1))
        self.assertTrue(is_valid_tree(tree2))
        self.assertTrue(is_valid_tree(tree3))
        self.assertFalse(is_valid_tree(tree4))

    def test_insert(self):
        nodes = [
            Node(2, 4),
            Node(-8, 0),
            Node(3, -1),
            Node(5, 1),
            Node(-2, 9),
            Node(7, -3),
            Node(-5, -7)
        ]
        tree = TwoDTree()
        tree.insert(2,4)
        tree.insert(-8,0)
        tree.insert(3,-1)
        tree.insert(5,1)
        tree.insert(-2,9)
        tree.insert(7,-3)
        tree.insert(-5,-7)


        self.assertEqual(nodes[0], tree.root)
        self.assertEqual(nodes[1], tree.root.lesser)
        self.assertEqual(nodes[2], tree.root.greater)
        self.assertEqual(nodes[3], tree.root.greater.greater)
        self.assertEqual(nodes[4], tree.root.lesser.greater)
        self.assertEqual(nodes[5], tree.root.greater.lesser)
        self.assertEqual(nodes[6], tree.root.lesser.lesser)
        self.assertTrue(is_valid_tree(tree))

    def test_exsits(self):
        tree1 = TwoDTree()
        tree1.root = Node(2,4)
        tree1.root.greater = Node(3,-1)
        tree1.root.lesser = Node(-8,0)
        tree1.root.greater.greater = Node(5,1)
        tree1.root.greater.lesser = Node(7,-3)
        tree1.root.lesser.greater = Node(-2, 9)
        tree1.root.lesser.lesser = Node(-5,-7)

        self.assertTrue(tree1.exists(2,4))
        self.assertTrue(tree1.exists(5,1))
        self.assertTrue(tree1.exists(-5,-7))
        self.assertFalse(tree1.exists(9,-7))
        self.assertFalse(tree1.exists(-5,7))

    def test_equals(self):
        tree1 = TwoDTree()
        tree1.root = Node(2,4)
        tree1.root.greater = Node(3,-1)
        tree1.root.lesser = Node(-8,0)
        tree1.root.greater.greater = Node(5,1)
        tree1.root.greater.lesser = Node(7,-3)
        tree1.root.lesser.greater = Node(-2, 9)
        tree1.root.lesser.lesser = Node(-5,-7)

        tree2 = TwoDTree()
        tree2.root = Node(2,4)
        tree2.root.greater = Node(3,-1)
        tree2.root.lesser = Node(-8,0)
        tree2.root.greater.greater = Node(5,1)
        tree2.root.greater.lesser = Node(7,-3)
        tree2.root.lesser.greater = Node(-2, 9)
        tree2.root.lesser.lesser = Node(-5,-7)

        tree3 = TwoDTree()
        tree3.root = Node(2,4)
        tree3.root.greater = Node(3,-1)
        tree3.root.lesser = Node(-8,0)
        tree3.root.greater.greater = Node(5,1)
        tree3.root.greater.lesser = Node(7,-3)
        tree3.root.lesser.greater = Node(-2, 9)

        tree4 = TwoDTree()

        self.assertTrue(tree1 == tree2)
        self.assertFalse(tree1 == tree3)
        self.assertFalse(tree4 == tree3)
        self.assertFalse(tree1 == tree4)

    def test_remove(self):
        tree1 = TwoDTree()
        tree1.insert(2,4)
        tree1.insert(-8,0)
        tree1.insert(3,-1)
        tree1.insert(5,1)
        tree1.insert(-2,9)
        tree1.insert(7,-3)
        tree1.insert(-5,-7)

        tree2 = TwoDTree()
        tree2.insert(-5,-7)

        tree3 = TwoDTree()
        tree3.insert(-8,0)
        tree3.insert(3,-1)
        tree3.insert(5,1)
        tree3.insert(-2,9)
        tree3.insert(7,-3)
        tree3.insert(-5,-7)

        tree1.remove(2,4)
        self.assertEqual(tree1, tree3)

        tree1.remove(-8,0)
        tree1.remove(3,-1)
        tree1.remove(5,1)
        tree1.remove(-2,9)
        tree1.remove(7,-3)
        self.assertEqual(tree1, tree2)

    def test_exists_in_area(self):
        tree1 = TwoDTree()
        tree1.root = Node(2,4)
        tree1.root.greater = Node(3,-1)
        tree1.root.lesser = Node(-8,0)
        tree1.root.greater.greater = Node(5,1)
        tree1.root.greater.lesser = Node(7,-3)
        tree1.root.lesser.greater = Node(-2, 9)
        tree1.root.lesser.lesser = Node(-5,-7)

        rect1 = [Point(-3,5), Point(-1,4), Point(-2,2), Point(-4,2)]
        rect2 = [Point(4,6), Point(1,6), Point(1,2), Point(4,2)]
        rect3 = [Point(5,3), Point(3,3), Point(3,1), Point(5,1)]

        self.assertFalse(tree1.exists_in_area(rect1))
        self.assertTrue(tree1.exists_in_area(rect2))
        self.assertTrue(tree1.exists_in_area(rect3))

#Recursive DFT of the tree to check each node is valid
def is_valid_tree(node, depth = 0):
    if isinstance(node, TwoDTree):
        return is_valid_tree(node.root)
    if not node:
        return True
    return is_valid_tree_node(node, depth) and is_valid_tree(node.greater, depth + 1) and is_valid_tree(node.lesser, depth + 1)
    

def is_valid_tree_node(node, depth):
    #x-aligned layer
    if(depth % 2 == 0):
        if node.greater:
            if not (node.greater.point.x >= node.point.x):
                return False
        if node.lesser:
            if not (node.lesser.point.x < node.point.x):
                return False
    #y-aligned layer
    else:
        if node.greater:
            if not (node.greater.point.y >= node.point.y):
                return False
        if node.lesser:
            if not (node.lesser.point.y < node.point.y):
                return False
    return True

if __name__ == "__main__":
    unittest.main()