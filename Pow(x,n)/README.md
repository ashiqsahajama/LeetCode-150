# LeetCode 50: Pow(x, n)

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/powx-n/)

Implement **pow(x, n)**, which calculates \( x^n \) (x raised to the power n).

### Constraints:
1. \( -100.0 < x < 100.0 \)
2. \( -2^{31} \leq n \leq 2^{31} - 1 \)
3. `n` is an integer.
4. Computations should be **optimized** for large `n`.

---

## Solution Explanation

This solution **uses recursion and fast exponentiation** (Exponentiation by Squaring).

### Steps:

1. **Base Case**:
   - If `n == 0`, return `1` (any number raised to `0` is `1`).
   - If `x == 0`, return `0` (0 raised to any power is `0`).

2. **Recursive Power Computation**:
   - If `n` is **even**, compute `helper(x, n // 2)` once and square it.
   - If `n` is **odd**, compute `helper(x, n - 1)` and multiply by `x`.

3. **Handle Negative `n`**:
   - Compute `helper(x, abs(n))`.
   - If `n` is negative, return `1 / result`.

---

## Code

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            if x == 0:
                return 0
            if n % 2 == 0:
                res = helper(x, n // 2)
                return res * res
            return x * helper(x, n - 1)
        
        a = helper(x, abs(n))
        return 1 / a if n < 0 else a
