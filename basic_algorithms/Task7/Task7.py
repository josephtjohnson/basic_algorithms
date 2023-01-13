## Represents a single node in the Trie
from logging import handlers


class RouteTrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.handler = None

    def insert(self, path_part):
        self.children[path_part] = RouteTrieNode()
        

## The Trie itself containing the root node and insert/find functions
class RouteTrie:
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
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route = RouteTrie()
        self.route.root.handler = root_handler
        self.route.not_found.handler = not_found_handler


    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_words  = self.split_path(path)
        print("path_l={}".format(path_words))
        self.route.insert(path_words, handler)



    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        #root case
        if path == '/':
            return self.route.root.handler

        path_words = self.split_path(path)
        print(path_words)
        if not self.route.find(path_words):
            return self.route.not_found.handler
        else:
            return self.route.find(path_words)



    def split_path(self,path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
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
