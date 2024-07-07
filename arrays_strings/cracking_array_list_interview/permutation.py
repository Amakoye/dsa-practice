# Permutation - Given two strings, write a function to check if one is a permutation of the other
# we'll do for lists in this case


def permutation(list1, list2):
    if len(list1) != len(list2):
        return False

    list1.sort()
    list2.sort()

    if list1 == list2:
        return True

    else:
        return False


list1 = [1, 2, 3]
list2 = [1, 3, 2]

print(permutation(list1, list2))
