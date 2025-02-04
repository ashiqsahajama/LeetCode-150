# LeetCode 226: Invert Binary Tree

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/invert-binary-tree/)

Given the `root` of a binary tree, invert the tree and return its root. Inverting a binary tree means swapping the left and right children of every node in the tree.

### Constraints:
1. The number of nodes in the tree is in the range `[0, 100]`.
2. \( -100 \leq \text{Node.val} \leq 100 \)

---

### Examples:

| Input                                   | Output                         |
|------------------------------------------|---------------------------------|
| `root = [4,2,7,1,3,6,9]`                 | `[4,7,2,9,6,3,1]`              |
| `root = [2,1,3]`                         | `[2,3,1]`                      |
| `root = []`                              | `[]`                           |

**Explanation for Example 1**:

The left and right children of each node are swapped.

---

## Solution Explanation

This solution uses a **recursive approach** to invert the binary tree.

### Steps:

1. **Base Case**:
   - If the `root` is `None`, return `None`.

2. **Swap Children**:
   - Swap the left and right children of the current node.

3. **Recursive Inversion**:
   - Recursively call the `invertTree` function on both the left and right subtrees.

4. **Return Result**:
   - Return the root node after all swaps are completed.

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Swap the left and right children
        temp = root.left
        root.left = root.right
        root.right = temp

        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return the inverted tree
        return root

