"""Union find/Disjoint set.

i : 0 1 2 3 4 5 6 7 8 # node
roots[i] : 0 1 2 3 4 5 6 7 8 # nodes root

1. are nodes connected,
  belong to the same tree/set
2. joins sets, trees."""

class UnionFind:
  """."""

  def __init__(self, num_nodes):
    self.roots = [i for i in range(num_nodes)]
    self.size = [1 for i in range(num_nodes)]


  def find_root(self, node_id):
    """Returns root of the node.
    
    root of i is roots[[[[...roots[i]...]]]]
    uses path compression to flatten trees"""
    if self.roots[node_id] != node_id:
      self.roots[node_id] = self.find_root(self.roots[node_id])
    return self.roots[node_id]
  # while self.roots[node_id] != node_id:
  #    next = self.roots[node_id] 
  #    self.roots[node_id] = self.roots[next]
  #    node_id = next
  # return self.roots[node_id]


  def union(self, left_id, right_id):
    """Quick-union - Joins two sets.
    
    adds smaller tree to a bigger one,
    aka quick-union"""
    left_root = self.find_root(left_id)
    right_root = self.find_root(right_id)
    if left_root == right_root:
      return
    
    left_size = self.size[left_id]
    right_size = self.size[right_id]
    # if left is bigger than right - swap
    # to set root of bigger set as a root of a smaller set
    if left_size > right_size:
      left_root, right_root = right_root, left_root
    self.roots[left_root] = right_root
    self.size[right_root] += left_size


  def connected(self, left_id, right_id):
    """True if nodes are in the same set/have same root."""
    return self.find_root(left_id) == self.find_root(right_id)

