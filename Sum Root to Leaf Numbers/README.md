# LeetCode 129: Sum Root to Leaf Numbers

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/sum-root-to-leaf-numbers/)

Given the `root` of a binary tree, each root-to-leaf path represents a number. You need to return the sum of all these numbers. The numbers are formed by concatenating the node values from root to leaf.

### Constraints:
1. The number of nodes in the tree is in the range `[1, 1000]`.
2. \( 0 \leq \text{Node.val} \leq 9 \)

---

### Examples:

**Example 1:**

| Input                                   | Output |
|------------------------------------------|--------|
| `root = [4,9,0,5,1]`                     | `1026` |

---

## Solution Explanation

This solution uses **Depth-First Search (DFS)** to traverse all paths from the root to the leaf nodes and calculate the sum of the numbers formed along each path.

### Steps:

1. **Define a Recursive DFS Helper Function**:
   - The helper function `dfs(node, val, res)` is responsible for traversing each node, building the path value, and adding the final value when a leaf node is reached.

2. **Handle Base Case**:
   - If the current node is `None`, return `0`.

3. **Build the Path Value**:
   - Append the current node's value to the string `val`.

4. **Check for Leaf Nodes**:
   - If the current node is a leaf (i.e., no left or right child), convert the string `val` to an integer and add it to `res`.

5. **Recursive Traversal**:
   - Continue the DFS traversal for the left and right subtrees, passing the updated `val`.

6. **Return the Result**:
   - The sum of numbers formed from all root-to-leaf paths is returned.

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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, val, res):
            if not node:
                return 0

            # Append the current node's value to the path string
            val += str(node.val)

            # If it's a leaf node, add the path value to the result
            if not node.left and not node.right:
                res += int(val)
                return res

            # Continue DFS on the left and right subtrees
            return dfs(node.left, val, res) + dfs(node.right, val, res)

        # Start DFS from the root node
        return dfs(root, "", 0)
