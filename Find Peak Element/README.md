# LeetCode 162: Find Peak Element

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/find-peak-element/)

A peak element is an element that is **strictly greater** than its neighbors.

Given an input array `nums`, find a **peak element** and return its **index**.  
If multiple peaks exist, return **any** peak's index.

### Constraints:
1. \( 1 \leq \text{nums.length} \leq 10^4 \)
2. \( -2^{31} \leq \text{nums[i]} \leq 2^{31} - 1 \)
3. `nums[i] != nums[i+1]` for all valid indices.

---

## Solution Explanation

This solution uses **Binary Search** to efficiently find a peak element.

### Steps:

1. **Initialize Pointers**:
   - `l = 0` (left boundary).
   - `r = len(nums) - 1` (right boundary).

2. **Perform Binary Search**:
   - Compute `mid = (l + r) // 2`.
   - If `nums[mid]` is **greater** than its left and right neighbors, return `mid` (it’s a peak).
   - If `nums[mid] < nums[mid + 1]`, move **right** (`l = mid + 1`).
   - Otherwise, move **left** (`r = mid - 1`).

3. **Return Peak Index**:
   - The algorithm **always** finds a peak due to the problem constraints.

---

## Code

```python
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            # Check if mid is a peak
            if (mid == 0 or nums[mid] > nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] > nums[mid + 1]):
                return mid
            # Move towards the higher element
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1
