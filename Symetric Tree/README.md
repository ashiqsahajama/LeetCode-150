# LeetCode 101: Symmetric Tree

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/symmetric-tree/)

Given the `root` of a binary tree, check whether it is a **mirror of itself** (i.e., symmetric around its center).

### Constraints:
1. The number of nodes in the tree is in the range `[0, 1000]`.
2. \( -100 \leq \text{Node.val} \leq 100 \)

---

### Examples:

| Input                                   | Output |
|------------------------------------------|--------|
| `root = [1,2,2,3,4,4,3]`                 | `true` |
| `root = [1,2,2,null,3,null,3]`            | `false` |

**Explanation for Example 1**:


---

## Solution Explanation

This solution uses a **recursive depth-first search (DFS)** approach to verify if the tree is symmetric.

### Steps:

1. **Define a Helper Function**:
   - The helper function `dfs(left, right)` compares two nodes to check if they are symmetric.

2. **Handle Base Cases**:
   - If both nodes are `None`, they are symmetric.
   - If one node is `None` and the other is not, they are not symmetric.

3. **Recursive Check**:
   - The nodes are symmetric if:
     - Their values are equal.
     - The left child of the left node matches the right child of the right node (`dfs(left.left, right.right)`).
     - The right child of the left node matches the left child of the right node (`dfs(left.right, right.left)`).

4. **Start the Recursion**:
   - Call `dfs` with the left and right children of the root node.

5. **Return Result**:
   - If all checks pass, return `True`.

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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            # Base cases
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            # Check values and recurse on mirrored children
            return (left.val == right.val and
                    dfs(left.left, right.right) and
                    dfs(left.right, right.left))

        # Start the recursion with the left and right children of the root
        return dfs(root.left, root.right)
