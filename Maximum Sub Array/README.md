# LeetCode 53: Maximum Subarray

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/maximum-subarray/)

Given an integer array `nums`, find the contiguous subarray (containing at least one number) that has the **largest sum**, and return its sum.

### Constraints:
1. \( 1 \leq \text{nums.length} \leq 10^5 \)
2. \( -10^4 \leq \text{nums[i]} \leq 10^4 \)

---

## Solution Explanation

This solution uses **Kadane’s Algorithm**, which is an efficient method for solving the **maximum subarray sum** problem in \( O(n) \) time complexity.

### Steps:

1. **Initialize Variables**:
   - `curr`: Tracks the running sum of the subarray.
   - `maxx`: Stores the maximum subarray sum found so far.

2. **Iterate Over Array**:
   - If `curr` (current sum) is negative, reset it to `0` (Kadane's optimization).
   - Add the current element to `curr`.
   - Update `maxx` to be the maximum of `maxx` and `curr`.

3. **Return the Maximum Subarray Sum**:
   - `maxx` stores the largest sum encountered during the traversal.

---

## Code

```python
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        maxx = nums[0]

        for i in nums:
            curr = max(curr, 0)
            curr += i
            maxx = max(maxx, curr)
            
        return maxx
