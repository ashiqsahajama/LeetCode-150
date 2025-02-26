# LeetCode 153: Find Minimum in Rotated Sorted Array

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

A **rotated sorted array** is an array that has been sorted in ascending order and then rotated at some pivot. Given such an array `nums`, find the **minimum element**.

### Constraints:
1. \( 1 \leq \text{nums.length} \leq 5000 \)
2. \( -5000 \leq \text{nums[i]} \leq 5000 \)
3. All elements in `nums` are **unique**.
4. `nums` was originally sorted in **increasing order** but may have been rotated.

---

## Solution Explanation

This solution uses **Binary Search** to efficiently locate the minimum element.

### Steps:

1. **Initialize Pointers**:
   - `i = 0` (left boundary).
   - `j = len(nums) - 1` (right boundary).

2. **Perform Binary Search**:
   - Compute `mid = (i + j) // 2`.
   - If `nums[mid] > nums[j]`, search **right** (`i = mid + 1`).
   - Else, search **left** (`j = mid`).

3. **Return the Minimum**:
   - `nums[i]` contains the smallest element after the loop ends.

---

## Code

```python
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1

        while i < j:
            mid = (i + j) // 2
            if nums[mid] > nums[j]:  # Minimum must be in right half
                i = mid + 1
            else:  # Minimum could be at mid or in left half
                j = mid

        return nums[i]  # Return the smallest element
