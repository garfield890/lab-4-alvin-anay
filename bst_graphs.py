import sys 
#import unittest 
from typing import List 
#from dataclasses import dataclass 
import math 
import matplotlib.pyplot as plt 
import numpy as np 
import random 
import time
sys.setrecursionlimit(10**6)

from bst import *
from bst_tests import *

TREES_PER_RUN : int = 10000
N_MAX = 50 

def float_ordering(val1 : float, val2 : float) -> bool:
    if val1 < val2:
        return True
    return False

# finds the height of a binary search tree
def height(bst : BinTree) -> int:
    match bst:
        case None:
            return 0
        case Node(_, l, r):
            return 1 + max(height(l), height(r))

# given a size n, function generates a bst of size n that contains floats from [0, 1]
def random_tree(n : int) -> BinarySearchTree:
    bst : BinarySearchTree = BinarySearchTree(float_ordering, None)
    for i in range(n):
        float_val = random.random()
        bst = insert(bst, float_val)
    return bst

# find average tree height of TREES_PER_RUN random trees of size n
def average_height(n : int) -> float:
    sum : float = 0.0
    for i in range(TREES_PER_RUN):
        bst : BinarySearchTree = random_tree(n)
        sum += height(bst.tree)
    return sum / TREES_PER_RUN

# calculates average time to insert random value into tree of size n
def average_time(n : int) -> float:
    sum : float = 0.0
    for i in range(TREES_PER_RUN):
        random_val = random.random()
        bst : BinarySearchTree = random_tree(n)

        start = time.perf_counter()
        bst = insert(bst, random_val)
        end = time.perf_counter()
        
        sum += (end - start)
    return sum / TREES_PER_RUN

# creates graph of average tree height based on n
def bst_graph() -> None:
    x_coords : List[int] = [ i for i in range(0, N_MAX + 1)]
    y_coords : List[float] = [ average_height(i) for i in x_coords]

    x_numpy : np.ndarray = np.array( x_coords )
    y_numpy : np.ndarray = np.array( y_coords )

    plt.plot(x_numpy, y_numpy, label='BST Performance')
    plt.xlabel("Size")
    plt.ylabel("Average Height")
    plt.title("Average Height of BST with Size N")
    plt.grid(True)
    plt.legend()
    plt.show()

# creates graph of time required based on n
def time_required_graph() -> None:
    x_coords : List[int] = [i for i in range(0, N_MAX + 1)]
    y_coords : List[float] = [average_time(i) for i in x_coords]

    x_numpy : np.ndarray = np.array( x_coords )
    y_numpy : np.ndarray = np.array( y_coords )

    plt.plot(x_numpy, y_numpy, label='Average Time')
    plt.xlabel("Size")
    plt.ylabel("Average Time")
    plt.title("Average Height for Inserting into BST")
    plt.grid(True)
    plt.legend()
    plt.show()


if (__name__ == '__main__'):
    time_required_graph()