# LeetCode 66: Plus One

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/plus-one/)

Given a **non-empty array of digits** representing a **non-negative integer**, increment the integer by **one**.

### Constraints:
1. The array represents a **non-negative** integer.
2. The most significant digit is at index `0`.
3. Each element in `digits` is between `0` and `9`.
4. No leading zeros, except for `0` itself.

---

## Solution Explanation

This solution **modifies the array in-place** to handle carry propagation.

### Steps:

1. **Iterate from the last digit (least significant)**:
   - If the digit is `9`, set it to `0` and **continue**.
   - Otherwise, increment the digit by `1` and return the modified list.

2. **Handle Overflow (All `9`s Case)**:
   - If all digits were `9`, the list becomes `[1]` followed by all `0`s.

---

## Code

```python
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits
