class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def append(self, value):
        new_node = Node(value)

        if self.isEmpty():
            self.head = new_node
            return

        # Traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        if self.isEmpty():
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        # Traverse through the linked list to find the node to delete
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def print_list(self):
        current = self.head

        while current:
            print(current.value, end="->")
            current = current.next
        print("None")


def main():
    ll = LinkedList()
    ll.append(10)
    ll.append(15)
    ll.print_list()
    ll.prepend(5)
    ll.print_list()
    ll.delete(10)

    ll.print_list()
    # print(ll.isEmpty())


if __name__ == "__main__":
    main()
