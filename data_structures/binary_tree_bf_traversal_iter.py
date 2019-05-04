"""Binary tree breadth first traversal."""

from queue import Queue


class Node:
  def __init__(self, left=None, right=None):
    self.left = left
    self.right = right

class Tree:
  def __init__(self, root):
    self.root = root

  def traverse(self, node):
    queue = Queue()
    queue.put(node)

    while not queue.empty():
      node = queue.get()
      if node.left:
        queue.put(node.left)
      if node.right:
        queue.put(node.right)
      print(node.data)
      

    

