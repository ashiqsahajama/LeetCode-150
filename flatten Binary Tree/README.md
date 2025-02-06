
# LeetCode 116: Populating Next Right Pointers in Each Node

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)

Given a perfect binary tree, populate each node's `next` pointer to point to its next right node. If there is no next right node, the `next` pointer should be set to `NULL`.


---

### Examples:

| Input                                   | Output |
|------------------------------------------|--------|
| `root = [1,2,3,4,5,6,7]`                 | `root = [1,#,2,3,#,4,5,6,7,#]` |

**Explanation for Example**:


The `next` pointers are populated to connect nodes on the same level.

---

## Solution Explanation

This solution uses a **Breadth-First Search (BFS)** approach to populate the `next` pointers level by level.

### Steps:

1. **Handle Base Case**:
   - If the tree is empty (`root = None`), return `None`.

2. **Initialize BFS**:
   - Use a queue (`deque`) to store nodes at each level.
   - Start by adding the `root` node to the queue.

3. **Traverse Level by Level**:
   - For each level, process all nodes currently in the queue.
   - Use the `next` pointer to link each node to the next node in the queue.
   - Add the left and right children of each node to the queue.

4. **Set Final `next` Pointers**:
   - The last node in each level should have its `next` pointer set to `NULL`.

5. **Return the Result**:
   - Return the modified tree.

---

## Code

```python
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque
from typing import Optional

class Solution:
    def connect(self, root: 'Node') -> Optional['Node']:
        if not root:
            return None

        # Initialize the BFS queue
        queue = deque([root])

        # Perform BFS to populate the next pointers
        while queue:
            lenq = len(queue)
            for i in range(lenq):
                node = queue.popleft()
                if i < lenq - 1:
                    node.next = queue[0]  # Link the current node to the next node in the queue

                # Add the children of the current node to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root
