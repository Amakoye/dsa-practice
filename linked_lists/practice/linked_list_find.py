from typing import Any


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c
c.next = d

""" 
Write a function, linkedListFind, that takes in the head of a linked list and a target value.
The function should return a boolean indicating whether or not the linked list contains the target.
"""


# Iterative way
# def linkedListFind(head: Node, target: Any) -> bool:
#     if head is None:
#         return False

#     current = head

#     while current:
#         if current.value == target:
#             return True
#         current = current.next

#     return False


# Recursive way
def linkedListFind(head: Node, target: Any) -> bool:
    if head is None:
        return False

    if head.value == target:
        return True

    return linkedListFind(head.next, target)


print(linkedListFind(a, "F"))
