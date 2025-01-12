# LeetCode 209: Minimum Size Subarray Sum

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/minimum-size-subarray-sum/)

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a contiguous subarray of which the sum is greater than or equal to `target`. If there is no such subarray, return `0`.

### Constraints:
1. `1 <= target <= 10^9`
2. `1 <= nums.length <= 10^5`
3. `1 <= nums[i] <= 10^5`

### Examples:

| Input                    | Output |
|--------------------------|--------|
| `target = 7, nums = [2,3,1,2,4,3]` | `2`    |
| `target = 4, nums = [1,4,4]`       | `1`    |
| `target = 11, nums = [1,1,1,1,1,1,1,1]` | `0` |

---

## Solution Explanation

This solution uses the **sliding window technique** to efficiently find the minimum size subarray that meets the condition:

1. **Initialize Variables**:
   - `i` is the left pointer of the sliding window.
   - `total` keeps track of the current sum of the window.
   - `m` stores the minimum length of the subarray, initialized to infinity (`float(inf)`).

2. **Expand the Window**:
   - Traverse the array with the right pointer `j`.
   - Add the value of `nums[j]` to `total`.

3. **Shrink the Window**:
   - While `total` is greater than or equal to `target`:
     - Update `m` to the minimum of `m` and the current window size (`j - i + 1`).
     - Subtract `nums[i]` from `total` and increment the left pointer `i` to shrink the window.

4. **Handle Edge Case**:
   - If no valid subarray is found, return `0`.

5. **Return Result**:
   - Return the value of `m` if it was updated, otherwise return `0`.

---
