# Accessing/Traversing a list
shoppingList = ["Milk", "Cheese", "Butter"]


# print(shoppingList[0])

# for i in shoppingList:
#     print(i)


# or
# for i in range(len(shoppingList)):
#     shoppingList[i] = shoppingList[i] + "+"

# print(shoppingList)

#  Update/Insert - List
myList = [1, 2, 3, 4, 5, 6, 7]

# myList[2] = 33

# print(myList)
# # add an element at the beginning/middle of the list
# myList.insert(0, 11)
# # add an element at the end
# myList.append(55)
# # add another list to our list
# newList = [11, 12, 13, 14]
# myList.extend(newList)
# print(myList)

# Slicing in a list
# print(myList[0:2])

# deletion
# myList.pop(1)
# del myList[0:2]

# print(myList)

# Searching in a list
myList2 = [10, 20, 30, 40, 50, 60, 70]

# in operator
# if 20 in myList2:
#     print(myList2.index(20))
# else:
#     print("The value does not exist")


# linear search
def searchInList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return "The value does not exist in the list"


# print(searchInList(myList2, 100))

# list operations/functions
# 1. concatenation
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)
# 2. * operator; repeats an element
# a = [0]
# a = a * 4
# print(a)

# functions
# 1. len() - returns the length of a list
# 2. max() - returns the item with the highest value in the List
# 3. min() - returns the item with the minimum value in the list
# 4. sum() - returns the sum of all items in the list
