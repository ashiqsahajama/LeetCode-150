# LeetCode 33: Search in Rotated Sorted Array

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/search-in-rotated-sorted-array/)

You are given an integer array `nums` sorted in **ascending order**, but it has been **rotated** at some pivot. Given a `target` value, return its **index** or `-1` if it is not found.

### Constraints:
1. \( 1 \leq \text{nums.length} \leq 5000 \)
2. \( -10^4 \leq \text{nums[i]}, \text{target} \leq 10^4 \)
3. `nums` has **unique elements**.

---

## Solution Explanation

This solution uses **Binary Search** to efficiently locate the `target` in a **rotated sorted array**.

### Steps:

1. **Initialize Pointers**:
   - `left = 0`, `right = len(nums) - 1`.

2. **Perform Binary Search**:
   - Compute `mid = (left + right) // 2`.
   - If `nums[mid] == target`, return `mid`.
   - Determine **which half is sorted**:
     - If `nums[mid] >= nums[left]`, the **left half is sorted**:
       - If `target` is within this half (`nums[left] ≤ target < nums[mid]`), search **left** (`right = mid - 1`).
       - Otherwise, search **right** (`left = mid + 1`).
     - Else, the **right half is sorted**:
       - If `target` is within this half (`nums[mid] < target ≤ nums[right]`), search **right** (`left = mid + 1`).
       - Otherwise, search **left** (`right = mid - 1`).

3. **Return Index or `-1`**:
   - If `target` is found, return its index.
   - Otherwise, return `-1`.

---

## Code

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Determine if left half is sorted
            if nums[mid] >= nums[left]:
                if target > nums[mid] or target < nums[left]:  
                    left = mid + 1  # Search right
                else:
                    right = mid - 1  # Search left
            else:  # Right half is sorted
                if target < nums[mid] or target > nums[right]:  
                    right = mid - 1  # Search left
                else:
                    left = mid + 1  # Search right

        return -1
