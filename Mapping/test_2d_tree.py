import unittest
from node import Node
from two_d_tree import TwoDTree

class TestTwoDTree(unittest.TestCase):

    def setUp(self):
        pass


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

    def test_exsits(self):
        pass

    def test_remove(self):
        pass

if __name__ == "__main__":
    unittest.main()