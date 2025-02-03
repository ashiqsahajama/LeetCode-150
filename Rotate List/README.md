# LeetCode 61: Rotate List

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/rotate-list/)

Given the `head` of a linked list, rotate the list to the right by `k` places.

### Constraints:
1. The number of nodes in the list is in the range `[0, 500]`.
2. \( -100 \leq \text{Node.val} \leq 100 \)
3. \( 0 \leq k \leq 2 \times 10^9 \)

---

### Examples:

| Input | Output |
|-------|--------|
| `head = [1,2,3,4,5], k = 2` | `[4,5,1,2,3]` |
| `head = [0,1,2], k = 4` | `[2,0,1]` |

**Explanation for Example 1**:


---

## Solution Explanation

This solution rotates the list by calculating the effective number of rotations using the list length:

### Steps:

1. **Calculate the Length of the List**:
   - Traverse the list to find the length (`n`) and the tail node.

2. **Determine the Effective Rotations**:
   - The effective number of rotations is `k % n`. If `k % n == 0`, no rotation is needed.

3. **Find the New Head**:
   - Traverse the list to the `(n - k)`-th node. This node's next node will become the new head of the rotated list.

4. **Update Pointers**:
   - Break the list at the `(n - k)`-th node.
   - Point the tail node's `next` to the original head to form the rotated list.

5. **Return the New Head**:
   - Return the new head node.

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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        # Step 1: Calculate the length of the list
        tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n += 1

        # Step 2: Determine the effective number of rotations
        k = k % n
        if k == 0:
            return head

        # Step 3: Find the new head
        cur = head
        for _ in range(n - k - 1):
            cur = cur.next

        # Step 4: Update pointers to form the rotated list
        newHead = cur.next
        cur.next = None
        tail.next = head

        # Step 5: Return the new head
        return newHead
