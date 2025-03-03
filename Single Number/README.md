# LeetCode 136: Single Number

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/single-number/)

Given a **non-empty** array of integers `nums`, every element **appears twice**, except for **one unique element**. Find and return the **single number**.

### Constraints:
1. \( 1 \leq \text{nums.length} \leq 3 \times 10^4 \)
2. \( -3 \times 10^4 \leq \text{nums[i]} \leq 3 \times 10^4 \)
3. Every number **except one** appears **exactly twice**.

---

## Solution Explanation

This solution uses the **XOR (^) bitwise operation**, which efficiently cancels out duplicate numbers.

### XOR Properties:
1. **Identity**: \( x \oplus 0 = x \)
2. **Self-Canceling**: \( x \oplus x = 0 \)
3. **Commutative & Associative**: Order does not matter.

### Steps:
1. **Initialize `res = 0`**.
2. **Iterate through `nums`**:
   - Perform `res ^= i` for each number `i`.
   - Since duplicates cancel out (`a ⊕ a = 0`), only the unique number remains.
3. **Return `res`**, which contains the single number.

---

## Code

```python
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i  # XOR cancels out duplicates
        return res
