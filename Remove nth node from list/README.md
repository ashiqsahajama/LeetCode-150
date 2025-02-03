# LeetCode 19: Remove Nth Node From End of List

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

Given the `head` of a linked list, remove the **n-th node from the end** of the list and return its head.

### Constraints:
1. The number of nodes in the list is in the range `[1, 30]`.
2. \( 0 \leq \text{Node.val} \leq 100 \)
3. \( 1 \leq n \leq \text{list.length} \)

### Examples:

| Input | Output |
|-------|--------|
| `head = [1,2,3,4,5], n = 2` | `[1,2,3,5]` |
| `head = [1], n = 1` | `[]` |
| `head = [1,2], n = 1` | `[1]` |

**Explanation for Example 1**:


---

## Solution Explanation

This solution removes the **n-th node from the end** in two main steps:

### Steps:

1. **Calculate the Length of the List**:
   - Use a pointer `curr` to traverse the list and count the total number of nodes (`m`).

2. **Find and Remove the Target Node**:
   - Use a second traversal to locate the node before the target node (position `m - n`).
   - Rewire the `next` pointer of the node before the target node to skip the target node.

3. **Return the Modified List**:
   - Return `dummy.next`, which points to the modified head of the list.

---

## Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Initialize a dummy node
        dummy = ListNode(0, head)
        curr = dummy

        # Step 2: Calculate the length of the list
        m = 0
        while curr:
            m += 1
            curr = curr.next

        # Step 3: Traverse to the node before the target node
        curr = dummy
        for _ in range(m - n - 1):
            curr = curr.next

        # Step 4: Remove the target node
        curr.next = curr.next.next

        # Step 5: Return the modified list
        return dummy.next
