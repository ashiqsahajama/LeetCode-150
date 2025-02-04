# LeetCode 82: Remove Duplicates from Sorted List II

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

Given the `head` of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

### Constraints:
1. The number of nodes in the list is in the range `[0, 300]`.
2. \( -100 \leq \text{Node.val} \leq 100 \)
3. The list is sorted in non-decreasing order.

### Examples:

| Input | Output |
|-------|--------|
| `head = [1,2,3,3,4,4,5]` | `[1,2,5]` |
| `head = [1,1,1,2,3]` | `[2,3]` |


---

## Solution Explanation

This solution removes all duplicate nodes from a sorted linked list using two pointers (`prev` and `curr`).

### Steps:

1. **Initialize Dummy Node**:
   - Create a dummy node pointing to the head of the list. This simplifies handling edge cases, such as removing the head node.

2. **Traverse the List**:
   - Use `curr` to traverse the list.
   - If a node has a duplicate (i.e., `curr.val == curr.next.val`), skip all nodes with that value.
   - Update `prev.next` to point to the next non-duplicate node.
   - If the current node has no duplicates, move `prev` forward.

3. **Handle End of List**:
   - Continue until all nodes are processed.

4. **Return the Result**:
   - Return `dummy.next`, which points to the modified list.

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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Initialize dummy node
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        # Step 2: Traverse the list
        while curr:
            if curr.next and curr.val == curr.next.val:
                # Skip all nodes with the same value
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next  # Skip the duplicate nodes
            else:
                prev = prev.next  # Move prev if no duplicates

            curr = curr.next  # Move curr to the next node

        # Step 3: Return the modified list
        return dummy.next


