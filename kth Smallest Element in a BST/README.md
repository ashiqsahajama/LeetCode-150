# LeetCode 230: Kth Smallest Element in a BST

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

Given the `root` of a **Binary Search Tree (BST)** and an integer `k`, return the **kth smallest element** in the BST.

### Constraints:
1. The number of nodes in the tree is in the range `[1, 10^4]`.
2. \( 0 \leq \text{Node.val} \leq 10^5 \).
3. The BST is guaranteed to have at least `k` elements.

---

## Solution Explanation

This solution uses **iterative inorder traversal** to find the `k`th smallest element in the BST. Since an inorder traversal of a BST results in a sorted sequence, the `k`th element in this sequence is the answer.

### Steps:

1. **Initialize Stack for Iterative Inorder Traversal**:
   - A stack is used to simulate the recursive traversal.

2. **Perform Inorder Traversal**:
   - Traverse to the leftmost node, pushing each node onto the stack.
   - Pop nodes from the stack one by one, incrementing a counter.
   - If the counter reaches `k`, return the current node's value.
   - Move to the right subtree and continue traversal.

3. **Return the kth Smallest Element**:
   - The loop ensures that exactly `k` elements are processed before returning the result.

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Stack for iterative inorder traversal
        stack = []
        node = root
        count = 0

        # Perform inorder traversal iteratively
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            count += 1

            # Return the kth smallest element
            if count == k:
                return node.val
            
            node = node.right
