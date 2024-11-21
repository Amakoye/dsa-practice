from typing import Optional, Union
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
        Prints the values in the linked list, helping with understanding traversal.

        Raises:
            Exception: If list is empty.

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

    def search(self, val:int, return_index:bool=False)->Union[bool, int]:

             
        """
        Finds the first occurence of a node by given value.

        Args:
            val (int): Value of the node to be searched.
            return_index (bool, optional): Whether to return the index instead of a boolean.


        Raises:
            ValueError: If the list is empty

        Returns:
            Union[bool, int]: Boolean indicating presence or index of the value
        """

        # Handle edge case: if the list is empty
        if self.head is None:
            raise ValueError("Linked list is empty")

        # If the node we're looking for is the head
        if self.head.val == val:
            return 0 if return_index else True

        # Traverse through list to find the node
        current = self.head
        index = 0

        while current:
            index+=1
            if current.val == val:
                return index if return_index else True
            current = current.next

        return -1 if return_index else False


    def delete(self, val:int)->None:
        """
         Deletes the first occurrence of a node with the given value.

        Args:
            val (int): Value of the node to be deleted.

        Raises:
            ValueError: If the list is empty or the node is not found.
        """

        # Handle edge case: if the list is empty
        if self.head is None:
            raise ValueError("Cannot complete delete operation. Linked list is empty!") 

        # If the node to be deleted is head
        if self.head.val == val:
            self.head = self.head.next
            print(f'Node ({val}) deleted successfully.')
            return

        # Traverse the list to find the node to delete
        current = self.head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
                print(f'Node ({val}) deleted successfully.')
                return

            current = current.next
        # Node not found
        raise ValueError(f'Node ({val}) Not found!')
        


    

        
