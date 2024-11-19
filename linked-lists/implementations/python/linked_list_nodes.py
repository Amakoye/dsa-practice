

from typing import Optional


class Node:
    """
    A node in a linked list data structure.

    Each node contains a value and a reference to the next node in the list.

    Basically represents a node in a singly linked list data structure.
    """
 
    def __init__(self, val:int=0, next:Optional['Node']=None) -> None:
        """
        Initializes a new node with the given value, and next node reference.

        Args:
            val (int, optional): The value to be stored in the node. Defaults to 0.
            next (Optional['Node'], optional): A reference to the next node in the linked list. 
                Defaults to None, indicating this node is the last in the list
        """
        self.val = val
        self.next = next

