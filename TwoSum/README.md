# LeetCode 1: Two Sum

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/two-sum/)

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

### Constraints:
1. \( 2 \leq \text{nums.length} \leq 10^4 \)
2. \( -10^9 \leq \text{nums[i]} \leq 10^9 \)
3. \( -10^9 \leq \text{target} \leq 10^9 \)
4. **Exactly one solution exists.**

### Examples:

| Input                     | Output  |
|---------------------------|---------|
| `nums = [2,7,11,15], target = 9` | `[1,0]` |
| `nums = [3,2,4], target = 6`     | `[2,1]` |
| `nums = [3,3], target = 6`       | `[1,0]` |

---

## Solution Explanation

This solution efficiently finds two numbers that sum to the target using a hash map:

1. **Initialize a Hash Map (`r`)**:
   - The dictionary stores values from `nums` as keys and their indices as values.

2. **Iterate Through the List**:
   - For each number in `nums`, calculate the complement `target - nums[i]`.
   - Check if the complement exists in the dictionary `r`:
     - If found, return the indices of the complement and the current number.
     - If not found, store the current number with its index in the dictionary.

3. **Return Result**:
   - The function returns a tuple with the indices of the two numbers.

---

## Code

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r = {}

        for i in range(len(nums)):
            if r.get(target - nums[i]) is not None:
                return (i, r[target - nums[i]])
            else:
                r[nums[i]] = i
