# LeetCode 104: Maximum Depth of Binary Tree

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

Given the `root` of a binary tree, return its **maximum depth**. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

### Constraints:
1. The number of nodes in the tree is in the range `[0, 10^4]`.
2. \( -100 \leq \text{Node.val} \leq 100 \)

---

### Examples:

| Input                                   | Output |
|------------------------------------------|--------|
| `root = [3,9,20,null,null,15,7]`         | `3`    |
| `root = [1,null,2]`                      | `2`    |
| `root = []`                              | `0`    |

**Explanation for Example 1**:


---

## Solution Explanation

This solution uses **Breadth-First Search (BFS)** to calculate the maximum depth level by level.

### Steps:

1. **Handle Base Case**:
   - If the tree is empty (`root` is `None`), return `0`.

2. **Initialize BFS**:
   - Use a queue (`deque`) to store nodes at each level.
   - Start by adding the `root` node to the queue.

3. **Traverse Level by Level**:
   - For each level, process all nodes currently in the queue.
   - Add the left and right children of each node to the queue.
   - Increment the depth counter (`level`) after processing each level.

4. **Return the Result**:
   - The final value of `level` gives the maximum depth of the tree.

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
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        level = 0

        # Perform BFS to calculate the maximum depth
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1  # Increment level after processing each level

        return level
