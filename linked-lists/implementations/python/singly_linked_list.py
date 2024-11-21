from typing import Optional
from linked_list_nodes import Node


class LinkedList:
    """
    Represents a singly linked list data structure.

    A singly linked list is a linear collection of nodes, where each node contains a value and a reference
    to the next node in the sequence. The list is traversed by following the next pointers from one node
    to the next.

    Operations.
    - Insertion at Head/Beginning
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


    def prepend(self, val:int)->None:
        """
        Inserts a node at the beginning. The node is treated as the head.

        Args:
            val (int): Represents the value/data to be stored in the node.
        """
        new_node = Node(val, self.head)
        self.head = new_node


    def append(self, val:int)->None:
        """
        Adds a new node to the end of the of the list.

        Args:
            val (int): Represents the value/data to be stored in the node.
        """
        current = self.head
        new_node = Node(val)

        # Handle edge case, if list is empty set the new node as the head
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the end of the list
        while current.next:
            current = current.next

        current.next = new_node

    def print_list(self)->None:
        """
        Prints the values in the linked list, helping with understanding traversal

        Raises:
            Exception: If list is empty

        Example output:
            0->1->2->3->None
        """

        if self.head is None:
            raise ValueError("Linked list is empty")
            

        current = self.head

        while current:
            print(current.val, end='->')
            current = current.next

        print("None")


    

        
