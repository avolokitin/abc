"""Binray heap."""

import heapq

class MinHeap:

  def __init__(self, nodes=None):
    self.nodes = list(nodes)
    
    for index in range(len(self.nodes) // 2):
      self.PercDown(index)
    
  
  def PercDown(self, index):
    """."""
    root = index
    left = (index * 2) + 1
    right = (index * 2) + 2

    if left < len(self.nodes) and self.nodes[left] < self.nodes[root]:
      root = left

    if right < len(self.nodes) and self.nodes[right] < self.nodes[root]:
      root = right
    
    if root != index:
      self.nodes[root] , self.nodes[index] = self.nodes[index], self.nodes[root]
      self.PercDown(index)

  def PercUp(self, index):

    left = index
    root = (index - 1) // 2

    if self.nodes[left] < self.nodes[root] and root >= 0:
      self.nodes[left], self.nodes[root] = self.nodes[root], self.nodes[left]
      self.PercUp(root)

  def __repr__(self):
    return '{}'.format(self.nodes)
    

  def Peek(self):
    return self.nodes[0]

  def Pop(self):
    """."""
    self.nodes[0], self.nodes[-1] = self.nodes[-1], self.nodes[0]
    smallest = self.nodes.pop()
    self.PercDown(0)
    return smallest

  
  def Push(self, val):
    """."""
    self.nodes.append(val)
    self.PercUp(len(self.nodes)-1)


nums = [1, 5, 2, 3, 4]
heap = MinHeap(nums)
print(heap)
heap.Pop()
print(heap)
heap.Push(1)
print(heap)

heapq.heapify(nums)
heapq.heappop(nums)
heapq.heappush(nums, 1)
print(nums)