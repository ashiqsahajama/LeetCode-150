# LeetCode 67: Add Binary

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/add-binary/)

Given two binary strings `a` and `b`, return their **sum** as a **binary string**.

### Constraints:
1. \( 1 \leq \text{a.length}, \text{b.length} \leq 10^4 \)
2. `a` and `b` consist **only** of `'0'` and `'1'`.
3. `a` and `b` do **not** contain leading zeros.

---

## Solution Explanation

This solution **simulates binary addition** using a **carry variable**.

### Steps:

1. **Initialize Variables**:
   - `carry = 0`: Stores carry-over from binary addition.
   - `res = []`: Stores the resulting binary sum.
   - `i, j = len(a)-1, len(b)-1`: Pointers to traverse from the least significant digit.

2. **Process Each Binary Digit**:
   - Convert `a[i]` and `b[j]` to integers (`0` if out of bounds).
   - Compute `total = c + d + carry`:
     - If `total % 2 == 1`, append `'1'`; otherwise, append `'0'`.
     - Compute the new `carry = total // 2`.
   - Decrease `i` and `j` to move **left** in `a` and `b`.

3. **Final Carry Check**:
   - If `carry` remains, append `'1'` to `res`.

4. **Return the Binary String**:
   - Reverse `res` since we built it **backwards**.

---

## Code

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = []
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            c = int(a[i]) if i >= 0 else 0
            d = int(b[j]) if j >= 0 else 0

            total = c + d + carry
            res.append(str(total % 2))
            carry = total // 2
            i -= 1
            j -= 1
        
        return "".join(res[::-1])
