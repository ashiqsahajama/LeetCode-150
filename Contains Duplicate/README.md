# LeetCode 219: Contains Duplicate II

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/contains-duplicate-ii/)

Given an integer array `nums` and an integer `k`, return `True` if there are two distinct indices `i` and `j` in the array such that:

- `nums[i] == nums[j]`
- The absolute difference between `i` and `j` is at most `k`.

### Constraints:
1. \( 1 \leq \text{nums.length} \leq 10^5 \)
2. \( -10^9 \leq \text{nums[i]} \leq 10^9 \)
3. \( 0 \leq k \leq 10^5 \)

### Examples:

| Input                           | Output  |
|---------------------------------|---------|
| `nums = [1,2,3,1], k = 3`        | `True`  |
| `nums = [1,0,1,1], k = 1`        | `True`  |
| `nums = [1,2,3,1,2,3], k = 2`    | `False` |

---

## Solution Explanation

This solution checks for nearby duplicates using a **sliding window set approach**:

1. **Initialize a Set and Pointers**:
   - Use a set `d` to track unique elements within the current sliding window.
   - Maintain a pointer `i` to track the left bound of the window.

2. **Traverse the Array**:
   - Iterate through the array with pointer `j`.
   - If the window size exceeds `k`, remove the leftmost element (`nums[i]`) and increment `i`.

3. **Check for Duplicates**:
   - If the current number `nums[j]` already exists in the set, return `True` (duplicate found within range `k`).
   - Otherwise, add the number to the set.

4. **Return Result**:
   - If no duplicate is found within `k` distance, return `False`.

---

## Code

```python
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = set()
        i = 0

        for j in range(len(nums)):
            if j - i > k and len(d) > 0:
                d.remove(nums[i])
                i += 1
            if nums[j] in d:
                return True
            d.add(nums[j])

        return False
