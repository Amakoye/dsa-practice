# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.


def searchInsertPos(array, target):
    if target in array:
        for i in range(len(array)):
            if array[i] == target:
                return i
    for i in range(len(array)):
        # check if we're at the last element
        if i == len(array) - 1:
            if array[i] < target:
                array.append(target)
                return len(array) - 1
            array.insert(i, target)
            return i

        if target < array[i]:
            array.insert(i + 1, target)
            return i
        elif target > array[i] and array[i + 1] > target:
            array.insert(i + 1, target)
            print(array)
            return i + 1


# nums = [1, 3, 5, 6]
# target = 5

# nums = [1, 3, 5, 6]
# target = 2

nums = [1, 3, 5, 6]
target = 0


print(searchInsertPos(nums, target))
