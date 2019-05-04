"""Iterative Binary tree traversal."""


class Node:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right
    

class Tree:
  def __init__(self, root):
    self.root = root

    