# LeetCode 21: Merge Two Sorted Lists

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/merge-two-sorted-lists/)

You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one **sorted** list. The merged list should be made by splicing together the nodes of the two input lists.

Return the head of the merged linked list.

### Constraints:
1. The number of nodes in both lists is in the range `[0, 50]`.
2. \( -100 \leq \text{Node.val} \leq 100 \)
3. Both `list1` and `list2` are sorted in **non-decreasing** order.

### Examples:

| Input | Output |
|-------|--------|
| `list1 = [1,2,4], list2 = [1,3,4]` | `[1,1,2,3,4,4]` |
| `list1 = [], list2 = []` | `[]` |
| `list1 = [], list2 = [0]` | `[0]` |

---

## Solution Explanation

This solution merges two sorted linked lists using a **dummy node and iterative approach**.

### Steps:

1. **Initialize a Dummy Node**:
   - Create a dummy node to simplify operations and serve as the head of the merged list.
   - Use a pointer `curr` to build the merged list.

2. **Merge Nodes**:
   - Traverse both linked lists.
   - Compare the current nodes of `list1` and `list2`.
   - Append the smaller node to the merged list and move the pointer forward.

3. **Handle Remaining Nodes**:
   - If one list is exhausted, append the remaining nodes from the other list to the merged list.

4. **Return the Result**:
   - Return `dummy.next`, which points to the head of the merged list.

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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy 

        # Merge nodes while both lists have elements
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        # Append any remaining nodes
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return dummy.next
