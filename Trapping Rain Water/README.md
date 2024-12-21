# LeetCode 150 Solutions

## Table of Contents
- [Trapping Rain Water](LeetCode/TrappingRainWater)

---

## Problem Explanations

### Trapping Rain Water

- **Problem:** [LeetCode Link](https://leetcode.com/problems/trapping-rain-water/)

  Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

---

### Solution Explanation

This solution uses the **Two Pointer Approach** to calculate the total amount of water trapped efficiently. 

1. **Key Observations**:
   - The amount of water trapped above a bar is determined by the minimum of the maximum heights to its left and right, minus the height of the bar itself.
   - Using two pointers (`i` and `j`), the algorithm keeps track of the left and right maximum heights as it traverses the elevation map.

2. **Two Pointers Logic**:
   - Start with pointers `i` at the beginning of the array and `j` at the end.
   - Maintain `max_l` and `max_r` to store the maximum heights encountered so far from the left and right, respectively.
   - At each step:
     - If the height at `i` is less than or equal to the height at `j`, update `max_l` and calculate the water trapped above the current bar at `i`.
     - Otherwise, update `max_r` and calculate the water trapped above the current bar at `j`.
   - Move the pointers inward until they meet.

3. **Final Result**:
   - The total amount of water trapped is accumulated in the variable `res`.

---
