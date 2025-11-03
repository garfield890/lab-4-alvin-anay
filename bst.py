import sys 
import unittest 
from typing import * 
from dataclasses import dataclass 
sys.setrecursionlimit(10**6)

BinTree: TypeAlias = Union[None, 'Node']
@dataclass(frozen=True)
class Node:
    value: Any
    left: BinTree
    right: BinTree

@dataclass(frozen=True)
class BinarySearchTree: 
    comes_before: Callable[[Any, Any], bool]
    tree: BinTree

# checks if binary search tree is empty
def is_empty(bst: BinarySearchTree) -> bool:
    return bst.tree == None

# inserts value into binary search tree using comes_before as comparator 
def insert(bst: BinarySearchTree, value: Any) -> BinarySearchTree:
    return BinarySearchTree(bst.comes_before, _insert(bst.tree, value, bst.comes_before))

def _insert(tree: BinTree, val: Any, comp: Callable[[Any, Any], bool]) -> BinTree:
    match tree:
        case None:
            return Node(val, None, None)
        case Node(v, l ,r):
            if comp(val, v):
                return Node(v, _insert(l, val, comp), r)
            else: 
                return Node(v, l, _insert(r, val, comp))
            
# checks if value is stored in BinarySearchTree
def lookup(bst: BinarySearchTree, value: Any) -> bool:
    return _lookup(bst.tree, value, bst.comes_before)

def _lookup(tree: BinTree, val: Any, comp: Callable[[Any, Any], bool]) -> bool:
    match tree:
        case None:
            return False
        case Node(v, l, r):
            if comp(val, v):
                return _lookup(l, val, comp)
            elif comp(v, val): 
                return _lookup(r, val, comp)
            else: 
                return True

# removes an elenment from a Binary Search Tree
def delete(bst: BinarySearchTree, value: Any) -> BinarySearchTree:
    return _delete(bst.tree, value, bst.comes_before)

def _delete(tree: BinTree, val: Any, comp: Callable[[Any, Any], bool]) -> BinTree: 
    match tree:
        case None: 
            return None
        case Node(v, l, r):
            if comp(val, v): 
                return Node(v, _delete(l, val, comp), r)
            elif comp(v, val):
                return Node(v, l, _delete(r, val, comp))
            else: 
                if l == None and r == None: 
                    return None
                elif l == None and r != None: 
                    return r
                elif l != None and r == None:
                    return l
                else: 
                    n = _find_smallest(r)
                    return Node()

def _find_smallest(tree: BinTree) -> Node: 
    if tree == None: 
        raise ValueError()
    l = tree.left
    r = tree.right
    if l == None and r == None:
        return Node(tree.value, l, r)
    else:
        return _find_smallest(l)