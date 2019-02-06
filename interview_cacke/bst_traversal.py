"""DF: in order traversal: left sub-tree - root - right sub-tree."""

class Node:

  def __init__(self, key, left=None, right=None):
    self.key = key
    self.left = left
    self.right = right

  def add_left(self, node):
    self.left = node
  
  def add_right(self, node):
    self.right = node

class Tree:
  
  def __init__(self, root):
    self.root = root

  def traverse_inorder(self, node=None):
    
    if node:
      if node.left:
        self.traverse_inorder(node.left)
      
      print(node.key)

      if node.right:
        self.traverse_inorder(node.right)
  
  def iterative_inorder(self, node):
    
    stack = [node]
    seen = set()
    
    while stack:
      current_node = stack[-1]
      if current_node.left and current_node.left not in seen:
        stack.append(current_node.left)
        continue
  
      current_node = stack.pop()
      seen.add(current_node)
      print(current_node.key)

      if current_node.right and current_node.right not in seen:
        stack.append(current_node.right)
        continue
      



a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
a.add_left(b)
a.add_right(c)
c.add_left(d)
c.add_right(e)
tree = Tree(a)

tree.iterative_inorder(tree.root)

