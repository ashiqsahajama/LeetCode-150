# LeetCode 530: Minimum Absolute Difference in BST

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

Given the `root` of a **Binary Search Tree (BST)**, return the minimum absolute difference between the values of any two nodes in the tree.

### Constraints:
1. The number of nodes in the tree is in the range `[2, 10^4]`.
2. \( 0 \leq \text{Node.val} \leq 10^5 \).

---

## Solution Explanation

This solution utilizes **inorder traversal** to process the BST nodes in sorted order. The minimum absolute difference is computed by comparing each node's value with the previous node's value.

### Steps:

1. **Initialize Variables**:
   - `prev`: Keeps track of the previously visited node during inorder traversal.
   - `res`: Stores the minimum absolute difference found.

2. **Perform Inorder Traversal**:
   - Inorder traversal (left -> root -> right) processes nodes in sorted order.
   - Compute the absolute difference between the current node and the previous node.
   - Update `res` with the minimum difference.

3. **Return the Minimum Difference**:
   - The function returns `res`, which contains the smallest absolute difference.

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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        res = float('inf')

        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            
            nonlocal prev, res
            if prev:
                res = min(res, node.val - prev.val)
            prev = node
            
            inorder(node.right)
            return res

        return inorder(root)
