from logging import handlers

class RouteTrieNode:
    """
    A class to represent a RouteTrieNode
    ...
    Attributes
    ----------
    children : dict
        a dictionary to map characters to words
    handler : string
        a response returned if path is terminal
    Methods
    -------
    insert(path_part):
        Takes a word within a url path and creates a new RouteTrieNode
    """
    
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.handler = None

    def insert(self, path_part):
        self.children[path_part] = RouteTrieNode()
        
     
class RouteTrie:
    """
    A class to represent a RouterTrieNode
    ...
    Attributes
    ----------
    root : RouteTrieNode
        a RouteTrieNode representing the root of the Trie
    not_found : RouteTrieNode
        a RouteTrieNode reprsenting a path that is not found
    Methods
    -------
    insert(path, handler):
        Takes a word within a url path and creates a new RouteTrieNode.
        The final word within the url path will have a handler assigned.
    find(path_list):
        Takes a word and returns all possible url paths that use that word
        as a root if contained within the Trie. Else it returns None.
    """
    
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = RouteTrieNode()
        self.not_found = RouteTrieNode()


    def insert(self, path, handler):
        ## Add a word to the Trie
        node =  self.root
        for word in path:
            if word not in node.children:
                node.children[word] = RouteTrieNode()                
                node  = node.children[word]
        node.handler = handler

        return node


    def find(self, path_list):
        ## Find the Trie node that represents this prefix
        node = self.root
        for path in path_list:
            if path not in node.children:
                return None
            else:
                node = node.children[path]
        return node.handler



# The Router class will wrap the Trie and handle 
class Router:
    """
    A class to represent a RouterTrieNode
    ...
    Attributes
    ----------
    route : RouteTrie
        a new RouteTrie
    root_handler : RouteTrieNode
        a RouteTrieNode reprsenting the root of the Trie
    not_found_handler : RouteTrieNode
        a RouteTrieNode representing when a url path is not found
    Methods
    -------
    add_handler(path, handler):
        Takes a path, splits the words within the path to add them to the trie.
        Assigns a handler to the final word in the path
    lookup(path):
        Takes a path and returns the associated handler or the not_found_handler
    split_path(path):
        Takes a path and splits it into a list of associated words
    """
    
    def __init__(self, root_handler, not_found_handler):
        self.route = RouteTrie()
        self.route.root.handler = root_handler
        self.route.not_found.handler = not_found_handler

    def add_handler(self, path, handler):
        path_words  = self.split_path(path)
        print("path_l={}".format(path_words))
        self.route.insert(path_words, handler)

    def lookup(self, path):
        if path == '/':
            return self.route.root.handler

        path_words = self.split_path(path)
        print(path_words)
        if not self.route.find(path_words):
            return self.route.not_found.handler
        else:
            return self.route.find(path_words)
        
    def split_path(self,path):
        path_words = path.split('/')
        output = []
        for word in path_words:
            if word.strip():
                output.append(word)
        return output
    
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
