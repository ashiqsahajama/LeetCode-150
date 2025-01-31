# LeetCode 92: Reverse Linked List II

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/reverse-linked-list-ii/)

Given the `head` of a singly linked list and two integers `left` and `right`, where \( 1 \leq \text{left} \leq \text{right} \leq \text{list.length} \), reverse the nodes of the list from position `left` to `right`, and return the modified list.

### Constraints:
1. The number of nodes in the list is in the range `[1, 500]`.
2. \( -500 \leq \text{Node.val} \leq 500 \)
3. \( 1 \leq \text{left} \leq \text{right} \leq \text{list.length} \)

---

### Examples:

| Input | Output |
|-------|--------|
| `head = [1,2,3,4,5], left = 2, right = 4` | `[1,4,3,2,5]` |
| `head = [5], left = 1, right = 1` | `[5]` |


---

## Solution Explanation

This solution uses **pointer manipulation** to reverse the specified section of the linked list.

### Steps:

1. **Initialize a Dummy Node**:
   - Create a dummy node pointing to the head of the list.
   - This simplifies handling edge cases (e.g., reversing from the head).

2. **Traverse to the `left` Position**:
   - Use a pointer `prevL` to track the node before the `left` position.
   - Use another pointer `curr` to track the node at the `left` position.

3. **Reverse the Sublist**:
   - Reverse the nodes between `left` and `right` using a temporary pointer (`p`).
   - For each node in the range, rewire the `next` pointer to point backward.

4. **Reconnect the Reversed Sublist**:
   - Reconnect the reversed sublist to the original list.
   - Update the pointers to link the node at position `left` to the node after `right`.

5. **Return the Result**:
   - Return `dummy.next`, which points to the head of the modified list.

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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Step 1: Initialize a dummy node
        dummy = ListNode(0, head)
        prevL = dummy
        curr = head

        # Step 2: Traverse to the `left` position
        for i in range(left - 1):
            prevL = curr
            curr = curr.next

        # Step 3: Reverse the sublist between `left` and `right`
        p = None
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = p
            p, curr = curr, temp

        # Step 4: Reconnect the reversed sublist
        prevL.next.next = curr
        prevL.next = p

        # Step 5: Return the modified list
        return dummy.next
