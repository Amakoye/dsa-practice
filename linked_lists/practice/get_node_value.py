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
Write a function, getNodeValue, that takes in the head of a linked list and an index. 
The function should return the value of the linked list at the specified index.

If there is no node at the given index, then return null.
"""


# Iterative way
# def getNodeValue(head: Node, index: int) -> Any:
#     if head is None:
#         return False

#     count = 0
#     current = head

#     while current:
#         if count == index:
#             return current.value
#         current = current.next
#         count += 1

#     return None


# Recursive way


def getNodeValue(head: Node, index: int) -> Any:
    if head is None:
        return None

    if index == 0:
        return head.value

    index -= 1

    return getNodeValue(head.next, index)


print(getNodeValue(a, 2))
