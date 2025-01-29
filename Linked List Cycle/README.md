# LeetCode 141: Linked List Cycle

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/linked-list-cycle/)

Given the `head` of a linked list, determine if the linked list contains a **cycle**.

A cycle occurs when a node's `next` pointer references an earlier node in the list, creating a loop.


### Examples:

| Input | Output |
|-------|--------|
| `head = [3,2,0,-4], pos = 1` | `True` |
| `head = [1,2], pos = 0` | `True` |
| `head = [1], pos = -1` | `False` |


---

## Solution Explanation

This solution detects cycles using the **Floyd’s Cycle Detection Algorithm** (also known as the **Tortoise and Hare Algorithm**).

### Steps:

1. **Initialize Two Pointers**:
   - `slow` moves **one step** at a time.
   - `fast` moves **two steps** at a time.

2. **Traverse the Linked List**:
   - If `fast` reaches `None` or the end of the list, return `False` (no cycle).
   - If `fast` and `slow` meet at any point, return `True` (cycle detected).

3. **Return the Result**:
   - If the traversal completes without meeting, return `False`.

---

## Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next  # Moves two steps
            slow = slow.next  # Moves one step
            if fast == slow:  # Cycle detected
                return True
        
        return False  # No cycle
