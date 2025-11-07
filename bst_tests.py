import sys 
import unittest 
from dataclasses import dataclass 
sys.setrecursionlimit(10**6) 
from bst import *

def int_ordering(val1 : int, val2 : int) -> bool:
    if (val1 < val2):
        return True
    return False

def str_ordering(str1 : str, str2 : str) -> bool:
    if (str1 < str2):
        return True
    return False

@dataclass(frozen=True)
class Point2:
    x : int
    y : int

def point_ordering(point1 : Point2, point2 : Point2) -> bool:
    if ( (point1.x ** 2 + point1.y ** 2) < (point2.x ** 2 + point2.y ** 2)):
        return True
    return False


class BSTTests(unittest.TestCase): 
    def test1(self): 
        bst1 : BinarySearchTree = BinarySearchTree(int_ordering, None)
        self.assertEqual(is_empty(bst1), True)
        bst2 : BinarySearchTree = BinarySearchTree(int_ordering, Node(4, None, None))
        self.assertEqual(is_empty(bst2), False)
        bst3 : BinarySearchTree = BinarySearchTree(int_ordering, Node(4, Node(3, Node(2, None, None), None), Node(5, None, Node(5, None, None))))
        self.assertEqual(is_empty(bst3), False)
    
    def test2(self):
        l1 = BinarySearchTree(int_ordering, Node(20, Node(3, Node(2, None, None), Node(6, None, None)), Node(80, None, Node(100, None, None))))
        r1 = BinarySearchTree(int_ordering, Node(20, Node(3, Node(2, None, None), Node(6, None, Node(10, None, None))), Node(80, None, Node(100, None, None))))
        self.assertEqual(insert(l1, 10), r1)

        l2 = BinarySearchTree(str_ordering, Node("aaaaa", Node("aaa", None, None), None))
        r2 = BinarySearchTree(str_ordering, Node("aaaaa", Node("aaa", None, None), Node("aaaaaa", None, None)))
        self.assertEqual(insert(l2, "aaaaaa"), r2)

        l3 = BinarySearchTree(point_ordering, None)
        r3 = BinarySearchTree(point_ordering, Node(Point2(10, 10), None, None))
        self.assertEqual(insert(l3, Point2(10, 10)), r3)

    def test3(self):
        bst1 : BinarySearchTree = BinarySearchTree(int_ordering, Node(4, Node(3, Node(2, None, None), None), Node(5, None, Node(5, None, None))))
        self.assertEqual(lookup(bst1, 2), True)
        bst2 : BinarySearchTree = BinarySearchTree(str_ordering, Node("d", Node("b", Node("a", None, None), Node("c", None, None)), Node("f", None, None)))
        self.assertEqual(lookup(bst2, "p"), False)
        bst3 : BinarySearchTree = BinarySearchTree(point_ordering, Node(Point2(4,5), Node(Point2(1,2), None, None), Node(Point2(56, 57), None, None)))
        self.assertEqual(lookup(bst3, Point2(56,57)), True)

    def test4(self):
        self.assertEqual(delete(BinarySearchTree(int_ordering, None), 25), BinarySearchTree(int_ordering, None))

        l1 = BinarySearchTree(int_ordering, Node(20, Node(3, Node(2, None, None), Node(6, None, None)), Node(80, None, Node(100, None, None))))
        r1 = BinarySearchTree(int_ordering, Node(20, Node(6, Node(2, None, None), None), Node(80, None, Node(100, None, None))))
        self.assertEqual(delete(l1, 3), r1)

        l2 = BinarySearchTree(str_ordering, Node("aaaaa", Node("aaa", None, None), Node("aaaaaa", None, None)))
        r2 = BinarySearchTree(str_ordering, Node("aaaaa", None, Node("aaaaaa", None, None)))
        self.assertEqual(delete(l2, "aaa"), r2)

        l3 = BinarySearchTree(point_ordering, Node(Point2(10, 10), None, None))
        r3 = BinarySearchTree(point_ordering, None)
        self.assertEqual(delete(l3, Point2(10, 10)), r3)

if (__name__ == '__main__'): 
    unittest.main() 