# LeetCode 201: Bitwise AND of Numbers Range

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/bitwise-and-of-numbers-range/)

Given two integers `left` and `right`, return the **bitwise AND** of all numbers in the range **[left, right]** (inclusive).

### Constraints:
1. \( 0 \leq \text{left} \leq \text{right} \leq 2^{31} - 1 \)

---

## Solution Explanation

This solution **shifts both numbers right** until they become equal, then shifts the result back.

### Key Idea:
- The bitwise `AND` of consecutive numbers **removes the rightmost differing bits**.
- We repeatedly **right shift** both numbers until `left == right`.
- Finally, **left shift** back to restore the removed bits.

### Steps:
1. **Initialize `i = 0`** (keeps track of shifts).
2. **Right Shift Until Equal**:
   - While `left != right`, shift both right (`>> 1`).
   - Increment `i` to count shifts.
3. **Left Shift Back**:
   - Shift `left` back `i` times (`<< i`) to restore lost bits.


Process:
- `left = 5 (101)`, `right = 7 (111)`, `i = 0`
- Shift right → `left = 2 (10)`, `right = 3 (11)`, `i = 1`
- Shift right → `left = 1 (1)`, `right = 1 (1)`, `i = 2`
- Shift back → `1 << 2 = 4`
- Result = `4`.

---

## Code

```python
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            i += 1
        return left << i


