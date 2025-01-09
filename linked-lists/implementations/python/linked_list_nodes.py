

from typing import Optional, TypeVar, Generic
#  ----------------------------------------------------------------------

T = TypeVar("T")

#  ----------------------------------------------------------------------



class Node(Generic[T]):
    """
    A node in a linked list data structure.

    Each node contains a value and a reference to the next node in the list.

    Basically represents a node in a singly linked list data structure.
    """
 
    def __init__(self, val:Optional[T]=None, next:Optional['Node']=None) -> None:
        """
        Initializes a new node with the given value, and next node reference.

        Args:
            val (int, optional): The value to be stored in the node.
            next (Optional['Node'], optional): A reference to the next node in the linked list. 
                Defaults to None, indicating this node is the last in the list
        """
        self.val = val
        self.next = next

#  ----------------------------------------------------------------------
class DoublyLinkedNode(Generic[T]):
    """
    Represents a node in a doubly linked list.

    Each node contains a value and references to both the next and previous nodes,
    allowing for bidirectional traversal of the list.
    
    Type Parameters:
        T: The type of value stored in the node.

    """
 
    def __init__(self, val:T, prev:Optional['DoublyLinkedNode[T]']=None, next:Optional['DoublyLinkedNode[T]']=None) -> None:
        """
        Initializes a new node with the given value and optional references to adjacent nodes.
        
        Args:
            val (T): The value to be stored in the node.

            prev (Optional[DoublyLinkedNode[T]]): Reference to the previous node. 
                Defaults to None, indicating this node is the first in the list.
                
            next (Optional[DoublyLinkedNode[T]]): Reference to the next node.
                Defaults to None, indicating this node is the last in the list.
        """
        self.val = val
        self.prev = prev
        self.next = next