def dnf_sort(array):
    """
    Receives an array of 0s, 1s, and 2, and returns a sorted array in a single traversal
 
    Parameters:
    arg1 (array): An unsorted, or sorted, array consisting of 0s, 1s, and 2s
  
    Returns:
    array: Sorted array
    """
    
    sorted_numbers = [[],[],[]]

    for i in range(0, len(array)):

        #if number in array is zero, add to first sub-array in sorted_numbers
        if array[i] == 0:
            sorted_numbers[0].append(array[i])
        
        #if number in array is one, add to second sub-array in sorted_numbers    
        if array[i] == 1:
            sorted_numbers[1].append(array[i])
        
        #if number in array is two, add to third sub-array in sorted_numbers    
        if array[i] == 2:
            sorted_numbers[2].append(array[i])

    #combine sub-arrays to return final result sorted as 0, 1, 2
    return sorted_numbers[0] + sorted_numbers[1] + sorted_numbers[2]

def test_function(test_case):
    sorted_array = dnf_sort(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
