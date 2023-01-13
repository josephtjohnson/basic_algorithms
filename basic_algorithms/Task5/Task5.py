from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.isEnd = False

    def suffixes(self, suffix = ''):
        ### Recursive function that collects the suffix for 
        ### all complete words below this point
        output = []
        for char, child in self.children.items():
            if child.isEnd:
                output.append(suffix + char)
            output.extend(child.suffixes(suffix + char))
        return output
        

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()


    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True


    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

interact(f,prefix='');
