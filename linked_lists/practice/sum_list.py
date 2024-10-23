from typing import List


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


a = Node(2)
b = Node(8)
c = Node(3)
d = Node(7)

a.next = b
b.next = c
c.next = d


""" 
Write a function, sumList, that takes in the head of a linked list containing numbers as an argument. 
The function should return the total sum of all values in the linked list.
"""


# Iterative way

# def sumList(head: Node) -> int:
#     _sum = 0

#     if head is None:
#         return

#     current = head

#     while current:
#         _sum += current.value
#         current = current.next

#     return _sum


# Recursion
def sumList(head: Node) -> int:
    if head is None:
        return 0

    return head.value + sumList(head.next)


print(sumList(a))
