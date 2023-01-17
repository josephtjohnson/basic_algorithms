from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact


class TrieNode:
    """
    A class to represent a TrieNode
    ...
    Attributes
    ----------
    children : dict
        a dictionary to map characters to words
    isEnd : boolean
        boolean used to determine if the character in the tree is a terminal one
        thus indicating a word
    Methods
    -------
    suffixes(suffix = ''):
        takes in a suffix an finds all possible words in the tree that start with
        that character.
    """

    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.isEnd = False

    def suffixes(self, suffix=""):
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
    """
    A class to represent a Trie.
    ...
    Attributes
    ----------
    root : TrieNode
        a TrieNode that will be the root of the Trie
    Methods
    -------
    insert(word):
        takes a word and associates each character in the word
        with the word.

    find(prefix):
        takes in a prefix and returns all possible words associated
        with it. If not words are associated with it, returns None.
    """

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
    "ant",
    "anthology",
    "antagonist",
    "antonym",
    "fun",
    "function",
    "factory",
    "trie",
    "trigger",
    "trigonometry",
    "tripod",
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != "":
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print("\n".join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print("")


print("\nTest 1")
print(f("a"))  # returns ['nt', 'nthology', 'ntagonist', 'ntonym', 'None']
print("///")

print("\nTest 2")
print(f(""))  # returns "None"
print("///")

print("\nTest 3")
print(f("z"))  # returns prefix +" not found" + "None"
print("///")

print("\nTest 4")
print(
    f(
        "zsadfkjhdasfkjbasergfonsdfgkjsdanguiadsfnoiauergnadfguinsigusndafiuangiousdrgbajsdfnaiuefnhaeriufna"
    )
)
# returns prefix + " not found" + "None"
print("///")

interact(f, prefix="")
