# LeetCode 112: Path Sum

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/path-sum/)

Given the `root` of a binary tree and an integer `targetSum`, return `true` if there is a **root-to-leaf path** where the sum of the node values equals `targetSum`. Otherwise, return `false`.

### Constraints:
1. The number of nodes in the tree is in the range `[0, 5000]`.
2. \( -1000 \leq \text{Node.val} \leq 1000 \)
3. \( -1000 \leq \text{targetSum} \leq 1000 \)

---

## Solution Explanation

This solution uses a **Depth-First Search (DFS)** approach to check if any root-to-leaf path has a sum that matches `targetSum`.

### Steps:

1. **Define a Recursive DFS Helper Function**:
   - The helper function `dfs(node, currsum)` traverses each node and keeps a running sum of node values along the path.

2. **Handle Base Case**:
   - If the current node is `None`, return `False`.

3. **Check for Leaf Node**:
   - If the current node is a leaf (i.e., no left or right child), check if `currsum + node.val` equals `targetSum`.

4. **Recursive Traversal**:
   - Continue the DFS traversal for the left and right children, passing the updated sum (`currsum + node.val`).

5. **Return Result**:
   - Return `True` if any path has a sum equal to `targetSum`, otherwise return `False`.

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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currsum):
            if not node:
                return False

            # Add the current node's value to the running sum
            currsum += node.val

            # If it's a leaf node, check if the path sum equals targetSum
            if not node.left and not node.right:
                return currsum == targetSum

            # Continue DFS on the left and right subtrees
            return dfs(node.left, currsum) or dfs(node.right, currsum)

        # Start DFS from the root node
        return dfs(root, 0)
