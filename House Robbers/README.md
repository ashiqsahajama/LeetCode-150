# LeetCode 198: House Robber

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/house-robber/)

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, but adjacent houses have security systems connected, so robbing two adjacent houses will alert the police.

Given an integer array `nums` representing the amount of money at each house, return the maximum amount you can rob without alerting the police.

### Constraints:
1. `0 <= nums.length <= 100`
2. `0 <= nums[i] <= 400`

### Examples:

| Input            | Output | Explanation |
|------------------|--------|-------------|
| `nums = [1,2,3,1]` | `4` | Rob house 1 (`1`) and house 3 (`3`) for a total of `1 + 3 = 4`. |
| `nums = [2,7,9,3,1]` | `12` | Rob house 1 (`2`), house 3 (`9`), and house 5 (`1`) for `2 + 9 + 1 = 12`. |
| `nums = [0]` | `0` | Only one house with `0` money, so the result is `0`. |

---

## Solution Explanation

This problem follows the **Dynamic Programming** approach:

1. **Base Cases**:
   - If there are no houses (`len(nums) == 0`), return `0`.
   - If there is only one house (`len(nums) == 1`), return `nums[0]`.

2. **Dynamic Programming Array**:
   - Define an array `robery` where `robery[i]` stores the maximum money that can be robbed up to house `i-1`.
   - Initialize:
     - `robery[0] = 0` (no house, no money)
     - `robery[1] = nums[0]` (only one house available to rob)

3. **Recurrence Relation**:
   - Iterate through the houses from index `1` to `len(nums)-1`.
   - At each step, choose between:
     - Not robbing the current house and keeping the previous max (`robery[i]`).
     - Robbing the current house and adding it to `robery[i-1]`.
   - Use the formula:  
     \[
     robery[i+1] = \max(robery[i], robery[i-1] + nums[i])
     \]
   - This ensures that no two adjacent houses are robbed.

4. **Final Output**:
   - The last element of `robery` gives the maximum amount that can be robbed.

---

## Code

```python
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        robery = [0] * (len(nums) + 1)
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        robery[0] = 0
        robery[1] = nums[0]
        for i in range(1, len(nums)):
            robery[i+1] = max(robery[i], robery[i-1] + nums[i])
        return robery[-1]
