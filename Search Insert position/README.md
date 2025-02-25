# LeetCode 35: Search Insert Position

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/search-insert-position/)

Given a **sorted** array of **distinct** integers `nums` and a target value `target`, return the **index** if the target is found. If not, return the index where it **would be inserted** in order.

### Constraints:
1. \( 1 \leq \text{nums.length} \leq 10^4 \)
2. \( -10^4 \leq \text{nums[i]}, \text{target} \leq 10^4 \)
3. `nums` contains **distinct** values in **ascending order**.

---

## Solution Explanation

This solution uses **Binary Search** to efficiently determine the position of `target`.

### Steps:

1. **Initialize Pointers**:
   - `i` (left) at `0`.
   - `j` (right) at `len(nums) - 1`.

2. **Perform Binary Search**:
   - Calculate `mid = (i + j) // 2`.
   - If `nums[mid] == target`, return `mid`.
   - If `nums[mid] < target`, move `i` to `mid + 1` (search right).
   - If `nums[mid] > target`, move `j` to `mid - 1` (search left).

3. **Return the Insert Position**:
   - If `target` is not found, return `i` (the correct insert index).

---

## Code

```python
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1

        return i  # Insert position
