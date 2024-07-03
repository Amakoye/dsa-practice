# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

import numpy as np


twoDArray = np.array(
    [[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]]
)

# newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=0)

print(twoDArray)

# print(newTwoDArray)


def accessElements(array, rowIndex, columnIndex):
    if rowIndex >= len(array) and columnIndex >= len(array[0]):
        print("Incorrect index")

    else:
        print(array[rowIndex][columnIndex])


def traverse2Darray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


def search2DArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == value:
                return f"value is located at {[i, j]}"
    return f"The element is not found"


# deletion
newTwoDArray2 = np.delete(twoDArray, 0, axis=0)
print(newTwoDArray2)

# print(search2DArray(twoDArray, 78))

# traverse2Darray(twoDArray)

# accessElements(twoDArray, 1, 2)
