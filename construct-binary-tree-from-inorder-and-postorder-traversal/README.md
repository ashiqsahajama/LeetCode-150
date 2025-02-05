# LeetCode 106: Construct Binary Tree from Inorder and Postorder Traversal

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

Given two integer arrays `inorder` and `postorder`, where `inorder` is the inorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree, construct and return the binary tree.

### Constraints:
1. The number of nodes in the tree is in the range `[0, 3000]`.
2. \( -3000 \leq \text{Node.val} \leq 3000 \)
3. Both `inorder` and `postorder` consist of **unique values**.
4. It is guaranteed that `inorder` and `postorder` are valid traversal sequences of a binary tree.

---

### Examples:

| Input                                   | Output                         |
|------------------------------------------|---------------------------------|
| `inorder = [9,3,15,20,7]`<br>`postorder = [9,15,7,20,3]` | Binary Tree: `root = [3,9,20,null,null,15,7]` |

**Explanation for Example**:


The last element of the postorder array (`3`) is the root of the tree. Using the inorder array, we find that `3` separates the left and right subtrees.

---

## Solution Explanation

This solution constructs the binary tree using a recursive helper function and two key concepts:
1. The **last element** of the postorder array is always the **root**.
2. The inorder array splits the tree into left and right subtrees.

### Steps:

1. **Create a Value-to-Index Map**:
   - To efficiently find the root's index in the inorder array, create a dictionary that maps each value to its index (`helpe`).

2. **Define a Recursive Helper Function**:
   - The helper function `helper(l, r)` constructs the tree for the inorder range `[l, r]`.

3. **Recursive Construction**:
   - Pop the last element from the `postorder` array to get the root node.
   - Find the index of this node in the inorder array (`mid`).
   - Recursively build the right and left subtrees:
     - Right subtree: `helper(mid + 1, r)`
     - Left subtree: `helper(l, mid - 1)`

4. **Return the Result**:
   - Start the recursion with the full inorder range and return the constructed tree.

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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Step 1: Create a value-to-index map for the inorder array
        helpe = {v: i for i, v in enumerate(inorder)}

        # Step 2: Define the recursive helper function
        def helper(l, r):
            if l > r:
                return None

            # Step 3: Pop the root value from the postorder array
            root = TreeNode(postorder.pop())

            # Step 4: Find the index of the root in the inorder array
            mid = helpe[root.val]

            # Step 5: Recursively build the right and left subtrees
            root.right = helper(mid + 1, r)
            root.left = helper(l, mid - 1)

            return root

        # Step 6: Start the recursion with the full inorder range
        return helper(0, len(inorder) - 1)
