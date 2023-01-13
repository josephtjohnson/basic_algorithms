

#Helper functions to sort the array 
from array import ArrayType


def findPivot(array, lowIndex, highIndex):

    pivot = array[highIndex]

    i = lowIndex - 1

    for j in range(lowIndex, highIndex):
        if array[j] <= pivot:

            i = i + 1

            (array[i], array[j]) = (array[j], array[i])


    (array[i + 1], array[highIndex]) = (array[highIndex], array[i + 1])

    return i + 1

def quick_sort(array, lowIndex, highIndex):
    if lowIndex < highIndex:

        pivot = findPivot(array, lowIndex, highIndex)

        quick_sort(array, lowIndex, pivot - 1)

        quick_sort(array, pivot + 1, highIndex)

    return [array]


def rearrangeArray (array):

    sorted_array = quick_sort(array, 0, len(array) - 1)

    first_number = ''
    second_number = ''

    for i in range(len(array) -1, 0, -2):
        first_number += str(sorted_array[0][i])
        second_number += str(sorted_array[0][i-1])
    first_number += str(sorted_array[0][0])
    final_array = [int(first_number), int(second_number)]
    return final_array


def test_function(test_case):
    output = rearrangeArray(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]

test_function([[1, 2, 3, 4, 5], [542, 31]])

test_function([[8, 0, 7, 1, 3], [831, 70]])

