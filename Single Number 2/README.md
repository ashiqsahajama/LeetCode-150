# LeetCode 137: Single Number II

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/single-number-ii/)

Given an integer array `nums` where **every element appears exactly three times**, except for **one element**, which appears **exactly once**, find and return the **single number**.

### Constraints:
1. \( 1 \leq \text{nums.length} \leq 3 \times 10^4 \)
2. \( -2^{31} \leq \text{nums[i]} \leq 2^{31} - 1 \)
3. Every element appears **three times**, except for one.

---

## Solution Explanation

This solution **uses bitwise operations** to efficiently count occurrences and extract the unique number.

### Key Idea:
- Since each number appears **three times**, we use two bit counters:
  - `ones`: Stores **bits appearing once**.
  - `twos`: Stores **bits appearing twice**.
- Bits appearing **three times** are cleared from both `ones` and `twos`.

### Steps:
1. **Iterate through `nums`**:
   - Update `ones` using:  
     ```ones = (ones ^ num) & ~twos```
   - Update `twos` using:  
     ```twos = (twos ^ num) & ~ones```
   - This ensures numbers appearing **three times** are removed from both counters.
2. **Return `ones`**:  
   - It contains the **unique number**.

---

## Code

```python
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones
