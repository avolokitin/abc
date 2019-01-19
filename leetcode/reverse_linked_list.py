"""Reverse a linked list in place."""

def reverse_list(head):
  """Disconnect head, make head.next=prev, make prev = current head,
  
  make new head = current head's.next.
  """
  prev = None
  while head:
    cur = head
    head = cur.next
    cur.next = prev
    prev = cur
  return prev