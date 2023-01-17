import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
        ints(list): list of integers containing one or more integers

    Returns:
        tuple containing the min and max of the list
    """

    min_value = 0
    max_value = 0

    for number in ints:
        if number <= min_value:
            min_value = number
        if number >= max_value:
            max_value = number

    return (min_value, max_value)


## Example Test Case of Ten Integers

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")  # pass

l = [i for i in range(0, 486)]  # a list containing 0 - 485
random.shuffle(l)

print("Pass" if ((0, 485) == get_min_max(l)) else "Fail")  # pass

l = [i for i in range(-47, 48)]  # a list containing -47 - 47
random.shuffle(l)

print("Pass" if ((-47, 47) == get_min_max(l)) else "Fail")  # pass
