//  ----------------------------------------------------------------------

/**
 * A node in a linked list data structure.
 * Each node contains a value and a reference to the next node in the list.
 * Basically represents a node in a singly linked list data structure.
 */
class SinglyLinkedNode<T> {
  value: T;
  next: SinglyLinkedNode<T> | null;

  /**
   * Initializes a new node with the given value, and next node reference.
   * @param value :The value to be stored in the node. Defaults to 0
   * @param next: A reference to the next node in the linked list.
   *    Defaults to null, indicating this node is the last in the list
   */
  constructor(value: T, next: SinglyLinkedNode<T> | null = null) {
    this.value = value;
    this.next = next;
  }
}

export { SinglyLinkedNode };
