"""Union find/Disjoint set.

i : 0 1 2 3 4 5 6 7 8 # node
roots[i] : 0 1 2 3 4 5 6 7 8 # nodes root

1. are nodes connected,
  belong to the same tree/set
2. joins sets, trees."""

class UnionFind:
  """."""

  def __init__(self, num):
    """Makes a new Set.
    
    By creating a new element with a unique id, a size of 1,
    and a parent pointer to itself.
    The parent pointer to itself indicates
    that the element is the representative member of its own set.
    O(n) - to init n sets
    """
    self.roots = [None] * num 
    self.size = [1] * num


  def FindRoot(self, node_id):
    """Returns id of a root node.
    
     follows the chain of parent pointers from node_id
     up the tree until it reaches a root element, whose parent is itself.
     This root element is the representative member
     of the set to which node_id belongs, and may be node_id itself.
     Path compression flattens the structure of the tree
     by making every node point to the root whenever Find is used on it
     O(M*N)
     """
     while node_id != self.roots[node_id]:
       next_node = self.roots[node_id]
       self.roots[node_id] = self.roots[next_node]
       node_id = next_node
    return self.roots[node_id]
    '''
    if node_id != self.roots[node_id]:
      self.roots[node_id] = self.FindRoot(self.roots[node_id])
    return self.roots[node_id]
    '''


  def IsConnected(self, left_node, right_node):
    """Returns True if sets are part of the same set."""
    return self.FindRoot(left_node) == self.FindRoot(right_node)


  def Union(self, left_node, right_node):
    """Joins to sets by size.
    
    Union(x,y) uses Find to determine the roots of the trees x and y belong to.
    If the roots are distinct, the trees are combined by attaching
    the root of one to the root of the other.
    Union by size always attaches the tree with
    fewer elements to the root of the tree having more elements.
    O(N + MlogN)
    """
    if self.IsConnected(left_node, right_node):
      return

    left_root = self.FindRoot(left_node)
    right_root = self.FindRoot(right_node)

    if self.size[left_root] < self.size[right_root]:
      self.roots[left_root] = right_root
      self.size[right_root] += self.size[left_root]
    else:
      self.roots[right_root] = left_root
      self.size[left_root] += self.size[right_root]


  
