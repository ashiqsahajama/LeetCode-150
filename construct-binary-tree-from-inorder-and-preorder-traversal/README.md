# LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

Given two integer arrays `preorder` and `inorder`, where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

### Constraints:
1. The number of nodes in the tree is in the range `[0, 3000]`.
2. \( -3000 \leq \text{Node.val} \leq 3000 \)
3. Both `preorder` and `inorder` consist of **unique values**.
4. It is guaranteed that `preorder` and `inorder` are valid traversal sequences of a binary tree.

---

### Examples:

| Input                                   | Output                         |
|------------------------------------------|---------------------------------|
| `preorder = [3,9,20,15,7]`<br>`inorder = [9,3,15,20,7]` | Binary Tree: `root = [3,9,20,null,null,15,7]` |

**Explanation for Example**:


The first element of the preorder array (`3`) is the root of the tree. Using the inorder array, we find that `3` separates the left and right subtrees.

---

## Solution Explanation

This solution constructs the binary tree using a recursive approach and two key concepts:
1. The **first element** of the preorder array is always the **root**.
2. The inorder array splits the tree into left and right subtrees.

### Steps:

1. **Base Case**:
   - If either the `preorder` or `inorder` array is empty, return `None`.

2. **Identify the Root**:
   - The first element of the `preorder` array is the root node.
   - Create a new `TreeNode` with this value.

3. **Split the Inorder Array**:
   - Find the index of the root node in the `inorder` array.
   - The left subtree corresponds to elements before this index in the `inorder` array.
   - The right subtree corresponds to elements after this index.

4. **Recursive Construction**:
   - Recursively construct the left subtree using:
     - `preorder[1:mid+1]` (next elements in preorder for the left subtree).
     - `inorder[:mid]` (left subtree elements in inorder).
   - Recursively construct the right subtree using:
     - `preorder[mid+1:]` (remaining elements in preorder for the right subtree).
     - `inorder[mid+1:]` (right subtree elements in inorder).

5. **Return the Result**:
   - Return the constructed root node.

---

## Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # Step 1: The first element of preorder is the root
        root = TreeNode(preorder[0])

        # Step 2: Find the root index in the inorder array
        mid = inorder.index(preorder[0])

        # Step 3: Recursively build the left and right subtrees
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        # Step 4: Return the constructed tree
        return root
