import SinglyLinkedList from "./singly_linked_list";

// Create a linked list for number operations
console.log("\n\n=== Number Operations Demo ===");
const numberList = new SinglyLinkedList<number>();

// Add some numbers
numberList.append(10);
numberList.append(20);
numberList.append(30);
numberList.append(40);
console.log("\nInitial number list:");
numberList.printList();

// Insert a number in the middle
numberList.insert_at(25, 2);
console.log("\nAfter inserting 25 at position 2:");
numberList.printList();

// Delete first and last numbers
numberList.delete_at(0); // Delete first
numberList.delete(40); // Delete last
console.log("\nAfter deleting first and last numbers:");
numberList.printList();
