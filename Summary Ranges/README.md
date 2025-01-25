# LeetCode 228: Summary Ranges

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/summary-ranges/)

You are given a **sorted unique integer array** `nums`. Return the **smallest sorted list of ranges** that cover all the numbers in the array exactly. That is, each element of `nums` is covered by exactly one of the ranges.

A range `[a,b]` is represented in the following format:

- `"a->b"` if `a != b`
- `"a"` if `a == b`

### Constraints:
1. \( 0 \leq \text{nums.length} \leq 20 \)
2. \( -2^{31} \leq \text{nums[i]} \leq 2^{31} - 1 \)
3. All the values of `nums` are **unique**.
4. `nums` is sorted in increasing order.

### Examples:

| Input               | Output                |
|-------------------- |---------------------- |
| `nums = [0,1,2,4,5,7]` | `["0->2","4->5","7"]` |
| `nums = [0,2,3,4,6,8,9]` | `["0","2->4","6","8->9"]` |
| `nums = []`          | `[]`                   |
| `nums = [-1]`        | `["-1"]`                |

---

## Solution Explanation

This solution iterates through the sorted list `nums` and identifies consecutive sequences to create range strings.

### Steps:

1. **Initialize Variables**:
   - `res`: Stores the result list of range strings.
   - `i`: Pointer to iterate through `nums`.

2. **Iterate Through `nums`**:
   - Set `s` to the starting number of the current sequence.
   - Use a nested `while` loop to extend the sequence as long as consecutive numbers are found.
   - If the range has more than one number, format it as `"start->end"`, otherwise, store it as `"start"`.

3. **Store Results**:
   - Append formatted ranges to the result list.

4. **Return Final Ranges**:
   - Return the constructed list of range strings.

---

## Code

```python
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0

        while i < len(nums):
            s = nums[i]
            
            while i < len(nums) - 1 and nums[i + 1] == nums[i] + 1:
                i += 1
            
            if s != nums[i]:
                res.append(str(s) + '->' + str(nums[i]))
            else:
                res.append(str(s))
            
            i += 1

        return res
