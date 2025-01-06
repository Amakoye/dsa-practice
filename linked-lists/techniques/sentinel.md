# Sentinel/Dummy Node.

## Overview

A sentinel or dummy node is an extra node that acts as a placeholder or a guard to simplify certain operations
It is not considered as part of the actual data structure but it is used to:

#### 1. Avoid edge cases:

- Operations like insertion or deletion at the head of the list often require special handling. The dummy node ensures that these operations can be performed uniformly,
  without extra checks for null or head references

#### 2. Simplifying code:

- It eliminates the need to check for special cases like an empty list, by ensuring there is always a node before the first element.

A sentinel node usually:

1. Has a default or null value.
2. Is created at the beginning and remains throughout the lifetime of the linked list.

## When to use

#### 1. Frequent Head Operations

- If the problem involves inserting, deleting, or processing nodes at the head of the list frequently.
- A sentinel node simplifies these operations by providing a uniform starting point.

#### 2. Avoiding special cases

- When you want to eliminate special case handling for an empty list, or the head node.
- It ensures all the nodes including the head are treated the same way.

#### 3. Complex logic for deletion/insertion

- If managing pointers for adjacent nodes is prone to errors (e.g `current.next == current.next.next`), a sentinel node can help clarify the logic and reduce bugs.

## When not to use

#### 1. Read only traversal

- If the operation only involves traversing the list or finding an element, a sentinel node doesn't provide any additional benefit.

#### 2. Perfomance constraints

- A sentinel node adds a small memory overhead, and might not be necessary for lightweight operations. For example inserting at the tail or searching for an element doesn't require it.

#### 3. Problem specific requirements

- If a problem explicitly requires operating directly on the list without modifying its structure (e.g interview problems/constrained environments) you may need to solve it without adding a sentinel.

## Example, Singly linked list implementation with a sentinel
