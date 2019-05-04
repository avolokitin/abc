"""
.
"""

class Node:
    
    nodes = {}  
    def __init__(self, value=0):
        self.value = value
        self.nodes = {}
    
    def add(self, n):
        self.nodes[n.value] = n
        
    def getNode(self, value):
        return self.nodes.get(value)
    
    def getValue(self):
        return value
    
    def addValue(self, str):
        new = self.nodes.get(str[0])
        if not new:
            new = Node(str[0])
            self.add(new)
    
        if len(str) > 1:
            new.addValue(str[1:])
            

def replace(source, dest, root):
    
    current_word = source
    current_parent = root
    while (current_word != dest):
    
        current_parent = root           
        for i in range(0, len(dest)):
            # go through every index    
            # lets try to replace the ith letter
            if (current_parent.getNode(dest[i])):
                trial_word = current_word[0:i] + dest[i] + current_word[i+1:]
                if (checkPath(current_parent.getNode(dest[i]), current_word[i+1:])):
                    current_word = trial_word
                    print (current_word)
            
            if (current_word == dest):
                break
            
            current_parent = current_parent.getNode(current_word[i])
            
            
            
def checkPath(node, word):
    for w in word:
        node = node.getNode(w)
        if not node:
            return False
    return True
        
    
if __name__ == '__main__':
    
    root = Node()
    words = ['dog', 'cot', 'cog', 'dot', 'dog']
    
    for w in words:
        root.addValue(w)
        
    replace("cat", "dog", root)