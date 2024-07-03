from array import *

# 1. Create array and traverse
my_array = array("i", [1, 2, 3, 4, 5, 6])


def traverseArray(array):
    for i in array:
        print(i)


# traverseArray(my_array)

# 2. Accessing individual elements through indexes
print("step 2")
print(my_array[0])

# 3. Append any value to the array using append() method
print("step 3")
my_array.append(7)
print(my_array)


# 4. Insert value in an array using insert() method
print("step 4")
my_array.insert(2, 10)
print(my_array)


# 5. Extend python array using extend() method
print("step 5")
my_array1 = array("i", [10, 11, 12])
my_array.extend(my_array1)
print(my_array)

# 6. Add items from list into an array using fromList() method
print("step 6")
tempList = [20, 21, 22]
my_array.fromlist(tempList)
print(my_array)
# 7. Remove an array element using remove() method
print("step 7")
my_array.remove(22)
print(my_array)
# 8. Remove last array element using pop() method
print("step 8")
my_array.pop()
print(my_array)
# 9. Fetch any element through its index using index() method
print("step 9")
print(my_array.index(20))
# 10. Reverse a python array using reverse() method
print("step 10")
my_array.reverse()
print(my_array)
# 11. Get array buffer information through buffer_info() method
print("step 11")
print(my_array.buffer_info())
# 12. Check for number of occurrences of an element using count() method
print("step 12")
print(my_array.count(12))
# 13. Convert array to string using toString() method
# print("step 13")
# strTemp = my_array.tostring()
# print(strTemp)
# 14. Convert array to a python list with the same elements using toList() method
# print("step 14")
# print(my_array.tolist())
# 15. Append a string to char array using fromString() method

# 16. Slice elements from an array
print("step 16")
# example on 3 elements
print(my_array[1:4])
