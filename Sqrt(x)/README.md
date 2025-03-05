# LeetCode 69: Sqrt(x)

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/sqrtx/)

Given a **non-negative integer `x`**, return the **square root of `x`** truncated to an integer.

### Constraints:
1. \( 0 \leq x \leq 2^{31} - 1 \)
2. The return value is the **integer part** of \( \sqrt{x} \) (i.e., no rounding up).

---

## Solution Explanation

This solution **uses binary search** to efficiently find the square root.

### Steps:

1. **Initialize Pointers**:
   - `l = 0`, `r = x` (search space for possible square roots).

2. **Binary Search for Square Root**:
   - Compute `m = (l + r) // 2`.
   - If `m * m == x`, return `m`.
   - If `m * m > x`, reduce search space (`r = m - 1`).
   - If `m * m < x`, increase search space (`l = m + 1`).

3. **Return `r`**:
   - If `m * m` is greater than `x`, `r` moves left.
   - `r` eventually holds the **integer square root**.

---

## Code

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x

        while l <= r:
            m = (l + r) // 2
            if m * m == x:
                return m
            if m * m > x:
                r = m - 1
            else:
                l = m + 1
        return r
