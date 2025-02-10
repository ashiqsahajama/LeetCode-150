# LeetCode 199: Binary Tree Right Side View

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/binary-tree-right-side-view/)

Given the `root` of a binary tree, return the values of the nodes that are visible from the **right side** of the tree. The right side view of a tree contains the last node at each level when viewed from the right.

### Constraints:
1. The number of nodes in the tree is in the range `[0, 100]`.
2. \( -100 \leq \text{Node.val} \leq 100 \)

---

## Solution Explanation

This solution uses **Breadth-First Search (BFS)** to traverse the tree level by level. At each level, the last node encountered is added to the result list, which represents the right side view of the tree.

### Steps:

1. **Handle Base Case**:
   - If the tree is empty (`root = None`), return an empty list.

2. **Initialize BFS**:
   - Use a queue (`deque`) to store nodes level by level.
   - Add the `root` node to the queue.

3. **Traverse Level by Level**:
   - For each level, traverse all nodes in the queue.
   - Append the value of the last node encountered at each level to the result list.
   - Add the left and right children of each node to the queue.

4. **Return the Result**:
   - The result list contains the values of the nodes visible from the right side of the tree.

---

## Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # Initialize the BFS queue
        q = deque([root])
        res = []

        # Perform BFS to collect right side view nodes
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # Add the last node's value at this level to the result
            res.append(node.val)

        return res
