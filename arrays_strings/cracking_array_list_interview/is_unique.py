# Is Unique - Implement an algorithm to determine if a list has all unique characters, using python list
myList = [1, 20, 30, 44, 5, 56, 57, 8, 19, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]


def isUnique(list):
    unique_list = []

    for i in range(len(list)):
        if list[i] not in unique_list:
            unique_list.append(list[i])

    print(len(unique_list) == len(list))


isUnique(myList)
