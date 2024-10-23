"""
Write a function, zipperLists, that takes in the head of two linked lists as arguments. 
The function should zipper the two lists together into single linked list by alternating nodes. 
If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. 
The function should return the head of the zippered linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty.

"""


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

x = Node("X")
y = Node("Y")
z = Node("Z")

a.next = b
b.next = c
c.next = d


x.next = y
y.next = z


# iterative way
# def zipperLists(head1: Node, head2: Node):
#     tail = head1
#     current1 = head1.next
#     current2 = head2

#     count = 0

#     while current1 and current2:
#         if count % 2 == 0:
#             tail.next = current2
#             current2 = current2.next
#         else:
#             tail.next = current1
#             current1 = current1.next
#         tail = tail.next
#         count += 1

#     if current1:
#         tail.next = current1

#     if current2:
#         tail.next = current2

#     return head1


# Recursive way
def zipperLists(head1: Node, head2: Node):
    if head1 is None and head2 is None:
        return None

    if head1 is None:
        return head2

    if head2 is None:
        return head1

    next1 = head1.next
    next2 = head2.next

    head1.next = head2
    head2.next = zipperLists(next1, next2)

    return head1
