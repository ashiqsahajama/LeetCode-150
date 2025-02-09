# LeetCode 236: Lowest Common Ancestor of a Binary Tree

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

Given a binary tree, find the **lowest common ancestor** (LCA) of two given nodes `p` and `q`. The lowest common ancestor of two nodes is the deepest node that has both `p` and `q` as descendants (where a node can also be a descendant of itself).

### Constraints:
1. The number of nodes in the tree is in the range `[2, 10^5]`.
2. The values of `p` and `q` are guaranteed to be present in the tree.
3. Each node in the tree has a unique value.

---

## Solution Explanation

This solution uses a **recursive DFS** approach to find the LCA by traversing each node and checking whether it is the ancestor of both `p` and `q`.

### Steps:

1. **Base Case**:
   - If the current node is `None`, return `None`.
   - If the current node is equal to either `p` or `q`, return the current node.

2. **Recursive Search**:
   - Recursively search for the LCA in the left and right subtrees.

3. **Determine the LCA**:
   - If both the left and right recursive calls return non-`None` values, the current node is the LCA.
   - If only one of the recursive calls returns a non-`None` value, propagate that result up the recursive call stack.

4. **Return the Result**:
   - Return the node identified as the LCA.

---

## Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if root is None, p, or q
        if not root or root == p or root == q:
            return root

        # Search for LCA in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right subtrees return non-None, current node is the LCA
        if left and right:
            return root

        # Otherwise, propagate the non-None result up
        return left or right
