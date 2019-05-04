"""."""
import os
import queue

class Dir:

  def __init__(self, subdirs=None, files=None):
    self.subdirs = subdirs or []
    self.files = files or []


def dir_bfs_traverse(_dir):
  queue = queue.Queue()
  queue.put(_dir)

  while not queue.empty():
    _dir = queue.get()
    for sub_dir in _dir.sub_dir:
      queue.put(sub_dir)
    for file in _dir.files:
      



def dir_dfs_traverse(_dir):
  stack = [_dir]
  size_path = {}
  visited = set()
  while stack:
    cur_dir = stack.pop()
    if cur_dir in visited:
      continue

    if cur_dir.subdirs:
      stack.append(cur_dir)
      for sub_dir in cur_dir.subdirs:
        stack.append(sub_dir)
        continue
    
    for file in cur_dir.files:
      visited.add(cur_dir)
      size = os.stat(file).st_size
      size_path['size'].append(file)

