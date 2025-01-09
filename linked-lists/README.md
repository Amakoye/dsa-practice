# Linked Lists

## Overview

A linked list is a linear data structure where each element points to the next element forming a sequence. Unlike arrays, linked list elements are not stored in contiguous memory locations.

## Types of Linked Lists

### 1. Singly Linked List

- Each node contains:
  - Data
  - Reference to next node
- Last node points to null
- Example:
  ```
  [1] -> [2] -> [3] -> null
  ```

### 2. Doubly Linked List

- Each node contains:
  - Data
  - Reference to next node
  - Reference to previous node
- Example:
  ```
  null <- [1] <-> [2] <-> [3] -> null
  ```

### 3. Circular Linked List

- Last node points back to first node
- Can be singly or doubly linked
- Example:
  ```
  [1] -> [2] -> [3] -> [1]
  ```

## Key Operations & Time Complexity

| Operation          | Time Complexity | Description                          |
| ------------------ | --------------- | ------------------------------------ |
| Insert at Head     | O(1)            | Add a node at the beginning          |
| Insert at Tail     | O(1)\*          | Add a node at the end                |
| Delete at Head     | O(1)            | Remove the first node                |
| Delete at Tail     | O(n)            | Remove the last node                 |
| Insert at Position | O(n)            | Add a node at specific position      |
| Delete at Position | O(n)            | Remove a node from specific position |
| Search             | O(n)            | Find a node by value                 |
| Traverse           | O(n)            | Visit all nodes                      |

\* O(1) with tail pointer

## Implementation Details

### Basic Node Structure

```python
# Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

```typescript
// TypeScript
class ListNode {
  data: number;
  next: ListNode | null;

  constructor(data: number) {
    this.data = data;
    this.next = null;
  }
}
```

## Common Patterns & Techniques

1. Two Pointer Technique
   - Fast & Slow Pointers
   - Leader/Follower Pattern
   - Left/Right Pattern
2. Dummy Node Usage

   - Handling edge cases
   - Simplifying operations

3. Runner Technique
   - Two pointers at different speeds
   - Used in cycle detection

## Edge Cases to Consider

- Empty list
- Single node
- Two nodes
- Cycle present
- No cycle
- Multiple cycles
- Lost reference

## Notes & Tips

- Always maintain proper references
- Consider using dummy nodes for edge cases
- Test with various input sizes
- Check for cycles before operations
- Remember to handle memory cleanup
