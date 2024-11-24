from typing import Generic, Optional, Union
from linked_list_nodes import DoublyLinkedNode, T

# --------------------------------------------------------------------------------------------------------------------------------------

class DoublyLinkedList(Generic[T]):
    """
    Represents a Doubly linked list data structure.

    A Doubly linked list is a linear collection of nodes, where each node contains a value and a reference
    to the next and previous node in the sequence. This allows for efficient traversal of the list in both directions.

    Operations.
    - Insertion at Head/Beginning
    - Insertion at Tail
    - Traversal
    - Delete at Head
    - Delete at Tail
    - Insert at a given Position
    - Delete at a given Position
    - Search

    Type Parameters:
        T: The type of value stored in the node.
    """

    def __init__(self, head:Optional[DoublyLinkedNode[T]]=None) -> None:
        """
         Initializes a Doubly linked list with the given node as the head.

        Args:
            head (Optional[DoublyLinkedNode[T]], optional): he first node in the list. Defaults to None if not provided, and 
                the list is initialized as empty.
        """
        self.head = head
        self.tail = head

    
    def prepend(self, val:T)->None:
        """
        Inserts a node at the beginning. The node is treated as the head.

        Args:
            val (T): Represents the value/data to be stored in the node.
        """
        new_node = DoublyLinkedNode[T](val)

        # Handle edge case if, list is empty.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return 

        new_node.next = self.head
        self.head.prev = new_node

        self.head = new_node
        

    def append(self, val:T)->None:
        """
        Inserts a node at the end. The node is treated as the tail.

        Args:
            val (T): Represents the value/data to be stored in the node.
        """
        new_node = DoublyLinkedNode[T](val)

        # Handle edge case, if list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node

        self.tail = new_node
        

    def print_list(self, reverse:Optional[bool]=False)->None:

        """
        Prints the values in the linked list, helping with understanding traversal.
        Supports both forward and reverse traversal.

        Args:
            reverse (Optional[bool]): If True, prints list from tail to head.
                If False (default), prints list from head to tail.

        Raises:
            ValueError: If list is empty.
        """

        # Handle edge case, if list is empty
        if self.head is None:
            raise ValueError("Linked list is empty!")

        if reverse:
            current = self.tail
            print("None", end="")

            while current:
                print(f" <- {current.val}", end="")
                current=current.prev
            print("None", end="")
        else:
            current = self.head

            print("None", end="")
            while current:
                print(f" -> {current.val}", end="")
                current = current.next
            print("None", end="")
    
    def search(self, val:T, return_index:bool=False)->Union[bool, int]:
        """
        Finds the first occurence of a node by given value.

        Args:
            val (T): Value of the node to be searched.
            return_index (bool, optional): Whether to return the index instead of a boolean.


        Raises:
            ValueError: If the list is empty

        Returns:
            Union[bool, T]: Boolean indicating presence or index of the value
        """        
        
        # Handle edge case, if list is empty
        if self.head is None:
            raise ValueError("Linked list is empty!")

     
        current = self.head
        count = 0

        while current:
            if  current.val == val:
                return count if return_index else True
            count +=1
            current = current.next

        return -1 if return_index else False

    def delete(self, val:T)->None:
        """
        Deletes the first occurrence of a node with the given value.

        Args:
            val (T): Value of the node to be deleted.

        Raises:
            ValueError: If the list is empty or the node is not found.
        """        
        # Handle edge case, if list is empty
        if self.head is None:
            raise ValueError("Linked list is empty!")

        # If the node to be deleted is head
        if self.head.val == val:
            # if there's only one node
            if self.head == self.tail:
                self.head = None
                self.tail = None

            else:
                self.head = self.head.next
                self.head.prev = None
            return
        
        current = self.head

        # Traverse to find the node
        while current and current.val != val:
            current= current.next

        # If item not found, current is none
        if current is None:
            raise ValueError("Item to be deleted not found!")

        # If the node to be deleted is the tail
        if self.tail.val == val and current==self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            return


        current.prev.next = current.next
        current.next.prev = current.prev



    