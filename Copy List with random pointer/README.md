# LeetCode 138: Copy List with Random Pointer

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/copy-list-with-random-pointer/)

A linked list is given where each node contains an integer `val`, a pointer to the next node (`next`), and a random pointer (`random`). The random pointer can point to any node in the list or `null`.

Your task is to create a **deep copy** of this list. A deep copy means that each node in the new list should have a new copy of both the `val` and pointers (i.e., `next` and `random`).

### Constraints:
1. \( 0 \leq \text{Number of nodes} \leq 1000 \)
2. \( -10^4 \leq \text{Node.val} \leq 10^4 \)

---

### Examples:

| Input                           | Output                     |
|---------------------------------|----------------------------|
| `[[7,null],[13,0],[11,4],[10,2],[1,0]]` | `[[7,null],[13,0],[11,4],[10,2],[1,0]]` |


---

## Solution Explanation

This solution uses a **hash map** to store the mapping between original nodes and their deep copies:

### Steps:

1. **Create Deep Copies of Nodes**:
   - Traverse the original list and create a copy of each node.
   - Use a hash map (`hash_map`) to store the mapping between each original node and its copy.

2. **Set Pointers**:
   - Traverse the list again.
   - For each node's copy, set the `next` and `random` pointers using the hash map.

3. **Return the Deep Copy**:
   - Return the deep copy of the head node.

---

## Code

```python
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Step 1: Create a hash map to store copies of nodes
        hash_map = {None: None}  # Handles null pointers

        # Step 2: First pass - create copies of all nodes
        curr = head
        while curr:
            copy_node = Node(curr.val)
            hash_map[curr] = copy_node
            curr = curr.next

        # Step 3: Second pass - set next and random pointers
        curr = head
        while curr:
            copy = hash_map[curr]
            copy.next = hash_map[curr.next]
            copy.random = hash_map[curr.random]
            curr = curr.next

        # Return the deep copy of the head node
        return hash_map[head]
