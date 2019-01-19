""" https://leetcode.com/problems/unique-email-addresses/ ."""
def NumUniqueEmails(emails):
  """
  :type emails: List[str]
  :rtype: int
  """
  seen = set()
  def _normalize(local):
    local_list = list()
    for char in local:
        if char == '+':
            break
        if char != '.':
          local_list.append(char)
    local = ''.join(local_list)
    return local
                         
  for addr in emails:
    local, domain = addr.split('@')
    local = _normalize(local)
    seen.add(('{}@{}'.format(local,domain)))
  return len(seen)

