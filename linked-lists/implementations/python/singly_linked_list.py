from typing import Optional
from linked_list_nodes import Node


class LinkedList:
    """
    Represents a singly linked list data structure.

    A singly linked list is a linear collection of nodes, where each node contains a value and a reference
    to the next node in the sequence. The list is traversed by following the next pointers from one node
    to the next.

    Operations.
    - Insertion at Head
    - Insertion at Tail
    - Traversal
    - Delete at Head
    - Delete at Tail
    - Insert at a given Position
    - Delete at a given Position
    - Search
    """

    def __init__(self, head:Optional[Node]=None) -> None:
        """
        Initializes a singly linked list with the given node as the head.

        Args:
            head (Optional[Node], optional): The first node in the list. Defaults to None if not provided, and 
                the list is initialized as empty.
        """
        self.head = head