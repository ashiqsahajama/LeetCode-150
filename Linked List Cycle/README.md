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

### Constraints:
1. The number of nodes in the list is in the range \( [0, 10^4] \).
2. \( -10^5 \leq \text{Node.val} \leq 10^5 \)
3. `pos` is the **index** where the tail of the list connects (if there is a cycle), otherwise `pos = -1`.

### Examples:

| Input | Output |
|-------|--------|
| `head = [3,2,0,-4], pos = 1` | `True` |
| `head = [1,2], pos = 0` | `True` |
| `head = [1], pos = -1` | `False` |

**Explanation for Example 1**:
