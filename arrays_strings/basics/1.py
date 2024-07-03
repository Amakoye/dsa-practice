from array import *


arr1 = array("i", [1, 2, 3, 4, 5, 6])
arr2 = array("d", [1.3, 1.23, 1.5])


# insertion operation
# at the end
# arr1.insert(6, 7)

# at the beginning
# arr1.insert(0, 0)

print(arr1)
# print(arr2)


def traverseArray(array):
    for i in array:
        print(i)


# traverseArray(arr1)


def accessElement(array, index):
    if index >= len(array):
        print("There is no any element in this index")

    else:
        print(array[index])


# accessElement(arr1, 1)
def searchInArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)

    return "The element does not exist in this array"


# print(searchInArray(arr1, 4))

# array deletion
arr1.remove(1)
print(arr1)
