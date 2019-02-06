"""You have a linked list and want to find the kth to last node.

Write a function kth_to_last_node() that takes an integer k and the head_node
of a singly linked list, and returns the kth to last node in the list.
"""

class Node:
  """Linked list node."""
  def __init__(self, value):
    self.value = value
    self.next = None

def kth_to_last_node(kth, head):
  """find the kth to last node."""
  length = 0
  current_node = head
  while current_node:
    length += 1
    current_node = current_node.next
  
  kth_node = head
  kth_node_index = length - kth 
  for _ in range(kth_node_index):
    kth_node = kth_node.next
  return kth_node.value