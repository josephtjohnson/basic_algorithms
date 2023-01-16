Description: The router implements the node class and a trie data structure to allow for multiple paths 
per letter of the word (e.g. a-n-t, a-r-k, a-b-e)

Time complexity: Even though the algorithm uses the dictionary data structure it still performs a 
breadth first search thus giving us an O(n)

Space complexity: Becasue we are creating a single trie and saving new nodes as they are produced, 
our space complexity remains linear O(n). New data structures are not being created depending upon the size of the input.
