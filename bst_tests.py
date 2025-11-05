import sys 
import unittest 
from typing import * 
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
    def test_example(self): 
        pass


if (__name__ == '__main__'): 
    unittest.main() 