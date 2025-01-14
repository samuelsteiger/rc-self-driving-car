import unittest
from node import Node
from two_d_tree import TwoDTree

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

        self.assertTrue(is_valid_tree(tree1))

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
        pass

    def test_remove(self):
        pass

def is_valid_tree(tree):
    queue = []
    queue.append(tree.root)
    depth = 0
    level_count = 1
    while len(queue) > 0:
        current_node = queue.pop(0)
        if current_node.greater:
            queue.append(current_node.greater)
            if depth % 2 == 0:
                if current_node.point.x >= current_node.greater.point.x:
                    return False
            else:
                if current_node.point.y >= current_node.greater.point.y:
                    return False
        level_count+=1
        if current_node.lesser:
            queue.append(current_node.lesser)
            if depth % 2 == 0:
                if current_node.point.x < current_node.lesser.point.x:
                    return False
            else:
                if current_node.point.y < current_node.lesser.point.y:
                    return False
        level_count+=1
        if 2**(depth+1) < level_count:
            depth+=1
            level_count = 1
    
    return True

if __name__ == "__main__":
    unittest.main()