from typing import Generic, Union, Optional
from linked_list_nodes import T, Node


class LinkedList(Generic[T]):
    """
    Represents an example implementation of a singly linked list, using a sentinel/dummy node

    Args:
        Generic (_type_): Represents the type for the list , i.e number, boolean, strings etc.

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

    def __init__(self)->None:
        """
        ;Initializes the linked list with a sentinel node and size counter.
        """
        self.sentinel= Node() # sentinel/dummy node
        self.size=0           # tracks the size of our lists


    def prepend(self, val:T)->None:
        """
        Inserts a node at the beginning of the list.
        
        Args:
            val (T): The value to be stored in the new node.
        """
        new_node = Node(val)
        new_node.next = self.sentinel.next
        self.sentinel.next = new_node
        self.size +=1


    def append(self, val:T)->None:
        """
        Adds a new node to the end of the of the list.

        Args:
            val (T): Represents the value/data to be stored in the node.
        """
        new_node = Node(val)
        current = self.sentinel

        while current.next:
            current = current.next

        current.next = new_node
        self.size +=1

    def print_list(self)->None:
        """
        Prints the linked list in a format: val1->val2->...->None
        Skips the sentinel node in the output.
        """
        current = self.sentinel.next # start at the first real node

        while current:
            print(current.val, end="->")
            current = current.next
        print('None')


    def delete(self, val:T)->None:
        """
         Deletes the first occurrence of a node with the given value.

        Args:
            val (T): Value of the node to be deleted.

        Raises:
            ValueError:  the node is not found.
        """

        current = self.sentinel

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
                self.size -=1
                print(f'Node ({val}) deleted successfully.')
                return
            current = current.next

         # Node not found
        raise ValueError(f'Node ({val}) Not found!')


    def insert_at(self, val:T, pos:int)->None:
        """
        Inserts a new node with the given value at the specified position.
        
        Args:
            val (T): Value to be inserted
            pos (int): Position where the value should be inserted (0-based)
            
        Raises:
            ValueError: If position is out of range
        """

        if pos < 0 or pos > self.size:
            raise ValueError(f"Cannot insert at position {pos}. Index is out of range!")

        new_node = Node(val)
        current = self.sentinel

        for _ in range(pos):
            current =current.next

        new_node.next = current.next
        current.next = new_node
        self.size+=1

    def delete_at(self, pos:int)->None:

        """
        Deletes the node at the specified position.
        
        Args:
            pos (int): Position of the node to delete (0-based)
            
        Raises:
            ValueError: If position is out of range or list is empty
        """


        if pos < 0 or pos>= self.size:
            raise ValueError(f"Cannot insert at position {pos}. Index is out of range!")

        if self.size == 0:
            raise ValueError("Cannot delete from empty list")
        
        current = self.sentinel

        for _ in range(pos):
            current=current.next

        current.next = current.next.next
        self.size -=1

    def search(self, val:T)->bool:
        """
        Searches for a value in the linked list.
        
        Args:
            val (T): The value to search for
            
        Returns:
            bool: True if value is found, False otherwise
        """
        current = self.sentinel.next

        while current:
            if current.val == val:
                return True
            current = current.next

        return False


        

