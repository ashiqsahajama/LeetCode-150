# LeetCode 191: Number of 1 Bits

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/number-of-1-bits/)

Given an **unsigned integer `n`**, return the **number of '1' bits** in its **binary representation** (also called **Hamming Weight**).

### Constraints:
1. \( 0 \leq n \leq 2^{31} - 1 \) (a 32-bit unsigned integer).

---

## Solution Explanation

This solution **counts the number of `1` bits** in `n` by repeatedly checking the **least significant bit** (LSB).

### Steps:

1. **Initialize `res = 0`** (stores the count of `1` bits).
2. **Iterate while `n` is not zero**:
   - If the **LSB** (`n % 2`) is `1`, increase `res`.
   - **Right shift (`n >> 1`)** to remove the last bit.
3. **Return `res`** after all bits are checked.

### Example:
For `n = 11` (binary: `1011`):
- `1011 % 2 = 1` → `res = 1`
- `101 % 2 = 1` → `res = 2`
- `10 % 2 = 0` → No change
- `1 % 2 = 1` → `res = 3`
- `n = 0`, stop.

---

## Code

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            if (n % 2) == 1:
                res += 1
            n = n >> 1  # Right shift to remove last bit
        return res
