# LeetCode 190: Reverse Bits

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/reverse-bits/)

Given a **32-bit unsigned integer** `n`, **reverse** its bits and return the resulting integer.

### Constraints:
1. `n` is a **32-bit unsigned integer**.
2. The output should be another **32-bit unsigned integer**.

---

## Solution Explanation

This solution **reverses the bits** of `n` using bitwise operations.

### Steps:

1. **Initialize `res = 0`** (stores the reversed bits).
2. **Iterate 32 times** (since `n` is a 32-bit integer):
   - Extract the **last bit** using `n & 1`.
   - **Shift `res` left** to make room for the new bit.
   - **Append the extracted bit** to `res` using `|`.
   - **Shift `n` right** to remove the last bit.
3. **Return `res`** after all bits are reversed.

### Example:
For `n = 00000010100101000001111010011100`:
- Reverse → `00111001011110000010100101000000`
- Output: `964176192`

---

## Code

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):  # Iterate through all 32 bits
            bit = n & 1  # Extract last bit
            res = (res << 1) | bit  # Shift left and append bit
            n = n >> 1  # Shift right to remove last bit
        return res
