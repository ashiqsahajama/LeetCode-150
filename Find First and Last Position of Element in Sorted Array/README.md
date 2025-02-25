# LeetCode 34: Find First and Last Position of Element in Sorted Array

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

Given an array of integers `nums` **sorted in non-decreasing order**, find the **starting and ending position** of a given `target` value.

If `target` is not found, return `[-1, -1]`.

### Constraints:
1. \( 0 \leq \text{nums.length} \leq 10^5 \)
2. \( -10^9 \leq \text{nums[i]} \leq 10^9 \)
3. `nums` is **sorted in non-decreasing order**.

---

## Solution Explanation

This solution uses **Binary Search** twice:
1. **First binary search** to find the **leftmost occurrence**.
2. **Second binary search** to find the **rightmost occurrence**.

### Steps:

1. **Binary Search Function (`binarysearch`)**:
   - Finds the first or last occurrence of `target` in `nums`.
   - If `left=True`, searches for the **leftmost** occurrence.
   - If `left=False`, searches for the **rightmost** occurrence.

2. **Find the First and Last Position**:
   - Call `binarysearch(nums, target, True)` for the left boundary.
   - Call `binarysearch(nums, target, False)` for the right boundary.

---

## Code

```python
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarysearch(nums, target, left):
            l, r = 0, len(nums) - 1
            i = -1  # Default to -1 if not found
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    i = mid  # Store index
                    if left:
                        r = mid - 1  # Search left half
                    else:
                        l = mid + 1  # Search right half
            return i
        
        left_idx = binarysearch(nums, target, True)
        right_idx = binarysearch(nums, target, False)
        return [left_idx, right_idx]
