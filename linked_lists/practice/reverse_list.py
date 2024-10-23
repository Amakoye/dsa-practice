from typing import Any, List


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
Write a function, reverseList, that takes in the head of a linked list as an argument. 
The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.
"""


# Iterative way
# def reverseList(head: Node) -> Any:
#     if head is None:
#         return

#     currrent = head
#     prev = None

#     while currrent:
#         _next = currrent.next
#         currrent.next = prev
#         prev = currrent
#         currrent = _next

#     return prev.value


# Recursion way
def reverseList(head: Node, prev: Node = None) -> Any:

    if head is None:
        if prev:
            return prev.value
        return None

    _next = head.next
    head.next = prev

    return reverseList(_next, head)

    # while currrent:
    #     _next = currrent.next
    #     currrent.next = prev
    #     prev = currrent
    #     currrent = _next

    return prev.value


print(reverseList(a))
