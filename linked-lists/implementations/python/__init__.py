from singly_linked_list import LinkedList

#  ----------------------------------------------------------------------
""" 
Singly linked list example
10->20->30->40->50->None
"""
linked_list=  LinkedList()

linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.print_list()
print(linked_list.search(40))
print(linked_list.search(40, return_index=True))
linked_list.prepend(40)
linked_list.print_list()
linked_list.insert_at(30, 2)
linked_list.print_list()
linked_list.delete_at(3)
linked_list.print_list()

#  ----------------------------------------------------------------------

def main():
    pass

if __name__ == "__main__":
    main()