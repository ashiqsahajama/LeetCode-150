
# LeetCode 2: Add Two Numbers

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/add-two-numbers/)

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the result as a linked list.

You may assume the two numbers do not contain any leading zero, except the number `0` itself.

### Constraints:
1. The number of nodes in each linked list is in the range `[1, 100]`.
2. \( 0 \leq \text{Node.val} \leq 9 \)
3. The input lists represent numbers without leading zeros, except for the number `0`.

### Examples:

| Input | Output |
|-------|--------|
| `l1 = [2,4,3], l2 = [5,6,4]` | `[7,0,8]` |
| `l1 = [0], l2 = [0]` | `[0]` |
| `l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]` | `[8,9,9,9,0,0,0,1]` |

---

## Solution Explanation

This solution adds two linked lists digit by digit, accounting for carry values:

### Steps:

1. **Initialize a Dummy Node**:
   - Create a dummy node to simplify operations and store the resulting list.
   - Use a pointer `cur` to build the result list.
   - Initialize `carry` to `0`.

2. **Iterate Through the Linked Lists**:
   - Add the values from both lists and the carry from the previous step.
   - Update the carry for the next step (`carry = val // 10`).
   - Create a new node with the current digit (`val % 10`) and link it to the result list.

3. **Move to the Next Nodes**:
   - Move `l1`, `l2`, and `cur` to their respective next nodes.
   - If one of the lists is exhausted, treat its value as `0`.

4. **Handle Final Carry**:
   - If a carry remains after processing both lists, create a new node for the carry.

5. **Return Result**:
   - Return `dummy.next`, which points to the head of the result list.

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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Calculate the sum and update carry
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10

            # Create a new node with the current value
            cur.next = ListNode(val)
            cur = cur.next

            # Move to the next nodes
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
