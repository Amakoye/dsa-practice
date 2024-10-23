from typing import List


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
Linked List values 
Write a function, linkedListValues, that takes in the head of a linked list as an argument. The function should return an array containing all values of the nodes in the linked list
"""

# Iterative way
# def linkedListValues(head: Node) -> List:
#     values = []

#     if head is None:
#         return []

#     current = head

#     while current:
#         values.append(current.value)
#         current = current.next

#     return values


# Recursion way
def linkedListValues(head: Node) -> List:
    values = []

    fillValues(head, values)

    return values


def fillValues(node: Node, values: List):
    if node is None:
        return values

    values.append(node.value)
    fillValues(node.next, values)


print(linkedListValues(a))
