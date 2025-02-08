# LeetCode 124: Binary Tree Maximum Path Sum

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

Given the `root` of a binary tree, return the maximum path sum. A **path** is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

### Constraints:
1. The number of nodes in the tree is in the range `[1, 3000]`.
2. \( -1000 \leq \text{Node.val} \leq 1000 \)

---

## Solution Explanation

This solution uses **Depth-First Search (DFS)** to calculate the maximum path sum. At each node, the algorithm computes:
1. The maximum path sum passing through that node (including both left and right subtrees).
2. The maximum path sum for the parent node's decision (either left or right subtree).

### Steps:

1. **Define a Recursive DFS Helper Function**:
   - The function `dfs(root)` traverses the tree and calculates the maximum path sum at each node.

2. **Handle Base Case**:
   - If the current node is `None`, return `0`.

3. **Calculate Path Sums**:
   - Recursively compute the maximum path sums for the left and right subtrees.
   - Ignore negative sums by setting any negative subtree sum to `0`.

4. **Update Global Result**:
   - The path sum through the current node (including both left and right subtrees) is compared with the global maximum path sum (`res`), and the maximum value is stored.

5. **Return Path Value**:
   - Return the maximum path sum including the current node and either the left or right subtree (but not both).

6. **Return Final Result**:
   - The result stored in `res[0]` is returned as the final answer.

---

## Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            # Recursively calculate the max path sums for the left and right subtrees
            leftmax = dfs(root.left)
            rightmax = dfs(root.right)

            # Ignore negative path sums
            leftmax = max(0, leftmax)
            rightmax = max(0, rightmax)

            # Update the global maximum path sum
            res[0] = max(res[0], leftmax + rightmax + root.val)

            # Return the maximum path sum for the current node
            return root.val + max(leftmax, rightmax)

        # Start DFS from the root node
        dfs(root)

        # Return the final maximum path sum
        return res[0]
