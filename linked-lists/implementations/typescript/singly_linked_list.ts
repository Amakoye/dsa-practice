import { SinglyLinkedNode } from "./linked_list_nodes";
//  ----------------------------------------------------------------------

/**
 *  Represents a singly linked list data structure.
 *  A singly linked list is a linear collection of nodes, where each node contains a value and a reference
    to the next node in the sequence. The list is traversed by following the next pointers from one node
    to the next.
    
*   Operations.
    - Insertion at Head/Beginning
    - Insertion at Tail
    - Traversal
    - Delete at Head
    - Delete at Tail
    - Insert at a given Position
    - Delete at a given Position
    - Search
 */
export default class SinglyLinkedList<T> {
  head: SinglyLinkedNode<T> | null;

  /**
   * Initializes a singly linked list with the given node as the head.
   * @param head: The first node in the list. Defaults to null if not provided, and 
        the list is initialized as empty.
   */
  constructor(head: SinglyLinkedNode<T> | null = null) {
    this.head = head;
  }

  /**
   * Adds a new node to the end of the of the list.
   * @param value: Represents the value/data to be stored in the node.
   */
  append(value: T): void {
    const newNode = new SinglyLinkedNode(value);

    // Handle edge case, if list is empty set the new node as the head
    if (this.head === null) {
      this.head = newNode;
      return;
    }

    // Traverse to the end of the list
    let current = this.head;

    while (current.next) {
      current = current.next;
    }

    current.next = newNode;
  }

  /**
   * Inserts a node at the beginning. The node is treated as the head.
   * @param value: Represents the value/data to be stored in the node.
   */
  prepend(value: T): void {
    const newNode = new SinglyLinkedNode(value);

    newNode.next = this.head;
    this.head = newNode;
  }

  /**
   * Prints the values in the linked list, helping with understanding traversal.
   */
  printList(): void {
    // Handle edge case, if list is empty set the new node as the head
    if (this.head === null) {
      throw new Error("Linked list is empty");
    }

    let current: SinglyLinkedNode<T> | null = this.head;
    let values: T[] = [];

    while (current) {
      values.push(current.value);
      current = current.next;
    }

    console.log(values.join("->"));
  }

  /**
   * Finds the first occurence of a node by given value.
   * @param value: Value of the node to be searched.
   * @param returnIndex): Whether to return the index instead of a boolean.
   * @returns: Boolean indicating presence or index of the value
   */
  find(value: T, returnIndex: boolean = false): boolean | number {
    // Handle edge case, if list is empty set the new node as the head
    if (this.head === null) {
      throw new Error("Linked list is empty");
    }

    // If the node we're looking for is the head
    if (this.head.value === value) {
      return returnIndex ? 0 : true;
    }

    // Traverse through the list to find the node
    let current: SinglyLinkedNode<T> | null = this.head;
    let count: number = 0;

    while (current) {
      if (current.value === value) {
        return returnIndex ? count : true;
      }
      current = current.next;
      count++;
    }

    return returnIndex ? -1 : false;
  }

  /**
   * Deletes the first occurrence of a node with the given value.
   * @param value: Value of the node to be deleted.
   * @returns
   */
  delete(value: T): void {
    // Handle edge case, if list is empty set the new node as the head
    if (this.head === null) {
      throw new Error("Linked list is empty");
    }

    // If the node we're looking for is the head
    if (this.head.value === value) {
      this.head = this.head.next;
      return;
    }

    // Traverse to find the node to delete
    let current: SinglyLinkedNode<T> | null = this.head;

    while (current) {
      if (current.next?.value === value) {
        current.next = current.next.next;
        return;
      }
      current = current.next;
    }

    throw new Error(`Node ${value} Not found!`);
  }

  /**
   * Adds a node at a given position or index.
   * @param value: Represents the value/data to be stored in the node.
   * @param index: Represents the index/position where the node should be inserted.
   */
  insert_at(value: T, index: number): void {
    const newNode = new SinglyLinkedNode<T>(value);
    // Handle edge case: negative index
    if (index < 0) {
      throw new Error("Index or posistion cannot be negative");
    }

    // Handle edge case: if List is empty and index is greater than 0
    if (this.head === null && index > 0) {
      throw new Error(
        "Cannot insert at position greater than 0 in an empty list"
      );
    }

    // Handle edge case: insert at the beginning, when index=0
    if (index === 0) {
      newNode.next = this.head;
      this.head = newNode;
      return;
    }

    // Otherwise, Traverse to find the node before the index
    let current = this.head;
    let count = 0;

    while (current && count < index - 1) {
      current = current.next;
      count++;
    }

    // Handle edge case: check if index is out of range and current is null
    if (current === null) {
      throw new Error(
        `Cannot insert at position ${index}. Index is out of range!`
      );
    }

    // insert the node
    newNode.next = current.next;
    current.next = newNode;
  }

  /**
   * Deletes a node at a given position/index.
   * @param index: Represents the index/position of the node to be deleted.
   */
  delete_at(index: number): void {
    // Handle edge case: negative index
    if (index < 0) {
      throw new Error("Index or posistion cannot be negative");
    }

    // Handle edge case: if List is empty and index is greater than 0
    if (this.head === null) {
      throw new Error(
        "Cannot complete delete operation. Linked list is empty!"
      );
    }

    // Handle edge case: delete at the beginning, when index=0
    if (index === 0) {
      this.head = this.head?.next;
      return;
    }

    // Otherwise, Traverse to find the node before the index
    let current: SinglyLinkedNode<T> | null = this.head;
    let count = 0;

    while (current && count < index - 1) {
      current = current.next;
      count++;
    }

    // Handle edge case: check if index is out of range and current is null
    if (current === null || current?.next === null) {
      throw new Error(
        `Cannot delete Node at position ${index}. Index is out of range!`
      );
    }

    current.next = current.next.next;
  }
}
