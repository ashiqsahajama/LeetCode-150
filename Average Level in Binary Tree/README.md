# LeetCode 637: Average of Levels in Binary Tree

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/average-of-levels-in-binary-tree/)

Given the `root` of a binary tree, return the average value of the nodes on each level in the form of a list. The average for each level is the sum of the node values divided by the number of nodes at that level.

### Constraints:
1. The number of nodes in the tree is in the range `[1, 10^4]`.
2. \( -10^5 \leq \text{Node.val} \leq 10^5 \)

---

## Solution Explanation

This solution uses **Breadth-First Search (BFS)** to traverse the tree level by level. At each level, the algorithm calculates the average of the node values and appends it to the result list.

### Steps:

1. **Initialize BFS**:
   - Use a queue (`deque`) to store nodes level by level.
   - Add the `root` node to the queue.

2. **Traverse Level by Level**:
   - For each level, calculate the sum of the node values and count the nodes.
   - Compute the average by dividing the sum by the count of nodes.
   - Append the average to the result list.
   - Add the left and right children of each node to the queue.

3. **Return the Result**:
   - The result list contains the average value of the nodes at each level.

---

## Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Initialize the BFS queue
        q = deque([root])
        result = []

        # Perform BFS to calculate averages at each level
        while q:
            level_sum = 0
            level_count = 0

            # Process all nodes at the current level
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                level_count += 1

                # Add the children of the current node to the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Calculate the average and append to the result list
            result.append(level_sum / level_count)

        return result
