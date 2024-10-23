""" 
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

    current = head

    while current:
        next_node = current.next

        while next_node and current.val == next_node.val:
            current.next = next_node.next
        current = current.next

    return head
