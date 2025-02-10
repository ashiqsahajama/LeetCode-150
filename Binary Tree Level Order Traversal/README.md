# LeetCode 102: Binary Tree Level Order Traversal

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/binary-tree-level-order-traversal/)

Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

### Constraints:
1. The number of nodes in the tree is in the range `[0, 2000]`.
2. \( -1000 \leq \text{Node.val} \leq 1000 \)

---

## Solution Explanation

This solution uses **Breadth-First Search (BFS)** to traverse the tree level by level. At each level, the algorithm collects the node values in a list and appends this list to the result.

### Steps:

1. **Handle Base Case**:
   - If the tree is empty (`root = None`), return an empty list.

2. **Initialize BFS**:
   - Use a queue (`deque`) to store nodes level by level.
   - Add the `root` node to the queue.

3. **Traverse Level by Level**:
   - For each level, create an empty list to store the node values.
   - Traverse all nodes currently in the queue.
   - Add the left and right children of each node to the queue.

4. **Store Level Results**:
   - Append the list of node values for each level to the result list.

5. **Return the Result**:
   - The result list contains the values of the nodes for each level.

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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initialize the result list
        result = []
        
        # Handle base case: empty tree
        if not root:
            return result

        # Initialize the BFS queue
        q = deque([root])

        # Perform BFS to collect node values at each level
        while q:
            level_values = []

            # Process all nodes at the current level
            for _ in range(len(q)):
                node = q.popleft()
                level_values.append(node.val)

                # Add the children of the current node to the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Append the current level's values to the result
            result.append(level_values)

        return result
