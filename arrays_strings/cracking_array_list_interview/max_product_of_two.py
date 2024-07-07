# Max product of two
# How to find maximum product of two integers in the array where all elements are positive


import numpy as np


myArray = np.array(
    [1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]
)


def maxProduct(array):
    previous = 0

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            current = array[i] * array[j]

            if current > previous:
                previous = current

    print(previous)


maxProduct(myArray)
