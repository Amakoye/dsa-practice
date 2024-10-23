class Node:
    """
    A node is the fundamental unit of a linked list. Each node will store data (a value) and a reference (or pointer) to the next node in the list.
    """

    def __init__(self, value) -> None:
        self.value = value  # The value stored in the node
        self.next = None  # Pointer to the next node, initially set to None


class LinkedList:
    """
    This class will manage the entire list. It will start with an empty list (i.e., no nodes), so the head of the list will initially be None.
    """

    def __init__(self) -> None:
        self.head = None  # Initially, the list is empty, so head is None

    # Insert method/Appending to the end
    def append(self, value):
        new_node = Node(value)

        # If the list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next

        # Append the new node
        current.next = new_node

    # Insert method/Insertion at the beginning
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Traversal method (Print all elements in the list)
    def print_list(self):
        current = self.head

        while current:
            print(current.value, end="->")
            current = current.next
        print("None")

    # Deletion of a node
    def delete(self, value):
        # if the list is empty/None
        if self.head is None:
            return

        # if the nodeto be deleted is the head
        if self.head.value == value:
            self.head = self.head.next
            return

        # Traverse the list to find the node to delete
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next


linked_list = LinkedList()

linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.print_list()

# linked_list.prepend(5)
# linked_list.print_list()

# linked_list.delete(20)
# linked_list.print_list()
