"""Recursive Binary tree traversal."""


class Node:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right
    

class Tree:
  def __init__(self, root):
    self.root = root
  
  def inorder(self, node):
    if not node:
     return

    if node.left:
      self.inorder(node.left)
    
    print(node.data)

    if node.right:
      self.inorder(node.right)