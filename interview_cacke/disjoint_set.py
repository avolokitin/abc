"""Disjoin-set."""

class DisjointSet:

  def __init__(self, num)
    self.roots = [None] * num
    self.size = [1] * num

  def FindRoot(self, node_id):

    if self.roots[node_id] != node_id:
      self.roots[node_id] = self.FindRoot(self.roots[node_id])
    return node_id

  def Connected(self, node_left, node_right):
    return self.FindRoot(node_left) == self.FindRoot(node_right)

  def Union(self, node_left, node_right):
    if self.Connected(node_left, node_right):
      return
    
    left_root = self.FindRoot(node_left)
    right_root = self.FindRoot(node_right)

    if self.size[left_root] < self.size[right]:
      self.roots[left_root] = right_root
      self.size[right_root] += self.size[left_root]
    else:
      self.roots[right_root] = left_root
      self.size[left_root] += self.size[right_root]