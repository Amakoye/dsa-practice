from singly_linked_list import LinkedList
from doubly_linked_list import DoublyLinkedList

#  ----------------------------------------------------------------------
""" 
Singly linked list example
10->20->30->40->50->None
"""
# linked_list:LinkedList['int']=  LinkedList()

# linked_list.append(10)
# linked_list.append(20)
# linked_list.append(30)
# linked_list.print_list()
# print(linked_list.search(40))
# print(linked_list.search(40, return_index=True))
# linked_list.prepend(40)
# linked_list.print_list()
# linked_list.insert_at(30, 2)
# linked_list.print_list()
# linked_list.delete_at(3)
# linked_list.print_list()

#  ----------------------------------------------------------------------

dl_linked_list:DoublyLinkedList['int']=DoublyLinkedList()
dl_linked_list.append(10)
dl_linked_list.append(20)
dl_linked_list.append(30)
dl_linked_list.print_list()
print()
dl_linked_list.print_list(reverse=True)
def main():
    pass

if __name__ == "__main__":
    main()