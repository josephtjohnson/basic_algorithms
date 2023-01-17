Description:
This algorithm performs a single traversal and determines the min and max of the data set. It accomplishes
this by storing the min and max values and only overwritting them if a more approriate value is found.


Time complexity: 
Because we are traversing the entire data set in a single pass our time complexity will be O(n).
Every item in the data set will have to be evaluated 1 time.

 
Space complexity:
Space complexity for this algorithm will be O(1). This is because regardless of the input, the space
utilized will always be the same. This determination is not taking into account that some numbers 
in a data set may require an int, float, or double. With this considered the space complexity will be
O(n).
