# LeetCode 128: Longest Consecutive Sequence

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/longest-consecutive-sequence/)

Given an unsorted array of integers `nums`, return the length of the **longest consecutive elements sequence**.

### Constraints:
1. \( 0 \leq \text{nums.length} \leq 10^5 \)
2. \( -10^9 \leq \text{nums[i]} \leq 10^9 \)

**Note:** The sequence must be consecutive numbers in ascending order, but the numbers can appear in any order in the input.

### Examples:

| Input                  | Output |
|------------------------|--------|
| `nums = [100,4,200,1,3,2]` | `4`    |
| `nums = [0,3,7,2,5,8,4,6,0,1]` | `9`    |
| `nums = []`             | `0`    |
| `nums = [1,2,0,1]`       | `3`    |


---

## Solution Explanation

This solution efficiently finds the longest consecutive sequence using a **set-based approach**:

### Steps:

1. **Convert the List to a Set**:
   - Store all unique numbers in a set to allow \( O(1) \) lookup time.

2. **Find the Start of a Sequence**:
   - Iterate through the numbers.
   - If `i - 1` is **not** in the set, it means `i` is the start of a new sequence.

3. **Expand the Sequence**:
   - Use a `while` loop to count the consecutive numbers by checking `i + 1` in the set.
   - Keep track of the length and update the maximum length found.

4. **Return the Longest Length**:
   - Return the maximum sequence length found.

---

## Code

```python
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        has = set(nums)  # Convert list to a set for O(1) lookups
        mx = 0

        for i in nums:
            m = 1
            # Only check sequences starting at the smallest number
            if i - 1 in has:
                continue
            while i + 1 in has:
                m += 1
                i += 1
            mx = max(m, mx)
            
        return mx
