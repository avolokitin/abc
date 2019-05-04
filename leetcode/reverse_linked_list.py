"""Reverse a linked list in place."""

class Node:
  """Linked List Node. """
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

def reverse_list(head):
  """Disconnect head,
  
  make head.next=prev,
  make prev = current head."""
  prev = None
  cur = head

  while cur:
    _next = cur.next
    cur.next = prev
    prev = cur
    cur = _next
  return prev