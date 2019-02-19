"""Given a linked list, determine if it has a cycle in it."""

def has_cycle(head):
  if not head or not head.next:
    return False
  
  slow = head
  fast = head.next

  while slow != fast:
    if fast is None or fast.next is None:
      return False
    slow = slow.next
    # making 2 steps at a time
    fast = fast.next.next 
  return True
