# LeetCode 172: Factorial Trailing Zeroes

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/factorial-trailing-zeroes/)

Given an **integer `n`**, return the **number of trailing zeroes** in `n!` (factorial of `n`).

### Constraints:
1. \( 0 \leq n \leq 10^4 \)
2. The function should run **efficiently** for large values of `n`.

---

## Solution Explanation

This solution **counts the number of factors of `5`** in `n!` because **each trailing zero comes from a factor of `10`**, which is produced by multiplying `2` and `5`.

### Key Observations:

1. A trailing zero is produced by a factor of **10** (`2 × 5`).
2. **Factors of 2 are more frequent** than factors of 5, so counting factors of 5 is enough.
3. Every multiple of `5` contributes at least **one factor of 5**.
4. Every multiple of `25` contributes **an extra factor of 5**.
5. Every multiple of `125` contributes **another extra factor of 5**, and so on.

### Steps:

1. **Initialize `count = 0`** to store the number of trailing zeroes.
2. **Iterate while `n ≥ 5`**:
   - Divide `n` by `5` (`n //= 5`).
   - Add `n` to `count` (counting how many times 5 is a factor).
3. **Return `count`**.

---

## Code

```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            n = n // 5
            count += n
        return count
