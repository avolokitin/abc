"""Trie/Prefix Tree.

Looking up entire words is easier with a hash table.
However, tries allow you to look up words by their prefixes,
something that hash tables cannot do because their keys are not split.
Build - O(m * n), n words, with m-largest word / m - num chars.
Trie doesn't need a has and thus a way to oversomce hash collisions
Can be used as an implemenation of assosiative array (hash-map) adt.

[Lexicographic sorting of a set of keys can be accomplished by building a trie from them,
and traversing it in pre-order, printing only the leaves' values.]

If all you wanted to do was to store words, a state machine might be easier.
However, the trie can store additional information for each word.
For example, the trie can store how popular a word might be.
That's why when you type "ye", "yes" is suggested before "yelling".
"""


class Node:
  def __init__(self, char=None, value=None):
    self.children = [None] * 26
    self.value = value
    self.key = char 
    self.end = False

  def __repr__(self):
    return '{} {}'.format(self.key, self.end)

class Trie: 
  def __init__(self):
    self.root = Node()
  
  def insert(self, word, value=None):
    """."""
    cur_node = self.root
    for char in word:
      char = char.lower()
      char_index = ord(char) - ord('a')
      if cur_node.children[char_index]:
        cur_node = cur_node.children[char_index]
      else:
        new_node = Node(char)
        cur_node.children[char_index] = new_node
        cur_node = new_node
    cur_node.value = value
    cur_node.end = True

  def get_longest_common_prefix(self):
    longest = 0
    prefix = '' 
    root_children = [child for child in self.root.children if child]
    for node in root_children:
      stack = [node]
      current_prefix = ''
      while stack:
        node = stack.pop()
        current_prefix += node.key
        node_children = [child for child in node.children if child]
        
        if node.end:
          prefix = max(prefix, current_prefix)
          break
        elif len(node_children) > 1:
          prefix = max(prefix, current_prefix)
          break
        else:
          stack.append(node_children[0])
    return prefix
        


  


trie = Trie()
trie.insert('cat')
trie.insert('dog')
trie.insert('do')
trie.insert('d')
trie.insert('cato')
trie.insert('catan')
print(trie.get_longest_common_prefix())