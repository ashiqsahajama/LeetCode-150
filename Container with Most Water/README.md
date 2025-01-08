# LeetCode 11: Container With Most Water

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/container-with-most-water/)

Given an array `height` of positive integers where each element represents the height of a vertical line at that index, find two lines that together with the x-axis form a container, such that the container can hold the most water.

### Constraints:
1. `n == height.length`
2. `2 <= n <= 10^5`
3. `0 <= height[i] <= 10^4`

### Examples:

| Input                        | Output |
|------------------------------|--------|
| `height = [1,8,6,2,5,4,8,3,7]` | `49`   |
| `height = [1,1]`             | `1`    |

---

## Solution Explanation

This solution uses the **two-pointer technique** to efficiently calculate the maximum area:

1. **Initialization**:
   - Start with two pointers:
     - `i` at the beginning of the array.
     - `j` at the end of the array.
   - Set `m` to `0` to track the maximum area.

2. **Calculate Area**:
   - For the current pair of lines (`i` and `j`):
     - Compute the area as `(j - i) * min(height[i], height[j])`.
     - Update `m` if this area is greater than the previous maximum.

3. **Move Pointers**:
   - Move the pointer corresponding to the shorter line inward:
     - If `height[i] <= height[j]`, increment `i`.
     - Otherwise, decrement `j`.

4. **Repeat Until Pointers Meet**:
   - Continue the process until `i` and `j` cross.

5. **Return Result**:
   - The maximum area `m` is returned.

---
