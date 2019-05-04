"""Given an undirected graph with maximum degree D,

find a graph coloring using at most D+1 colors."""

import queue 

class GraphNode:

  def __init__(self, label):
    self.label = label
    self.neighbors = set()
    self.color = None


COLORS = ['red', 'green', 'blue', 'yellow', 'orange']


def get_color(node, colors=COLORS):
  nc = set()
  for gn in node.neighbors:
    nc.add(gn.color)
  for color in colors:
    if color not in nc:
      return color

def color_graph(root, colors=COLORS[:3]):
  _queue = queue.Queue()
  _queue.put(root)
  visited = set()
  while not _queue.empty():
    node = _queue.get()
    if node in visited:
      continue

    visited.add(node)
    node.color = get_color(node)
    for gn in node.neighbors:
      _queue.put(gn)


a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')
d = GraphNode('d')

a.neighbors.add(b)
a.neighbors.add(d)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(b)
c.neighbors.add(d)
d.neighbors.add(a)
d.neighbors.add(c)




color_graph(a)
graph = [a, b, c, d]
for node in graph:
  print(node.color)