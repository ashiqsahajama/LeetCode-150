# LeetCode 150 Solutions

## Table of Contents
- [Jump Game](LeetCode/JumpGame)

---

## Problem Explanations

### Jump Game

- **Problem:** [LeetCode Link](https://leetcode.com/problems/jump-game/)

  You are given an integer array `nums` where `nums[i]` represents the maximum number of steps you can jump forward from that position. 

  Return `true` if you can reach the last index, or `false` otherwise.

---

### Solution Explanation

The solution uses a **Greedy Algorithm** to determine if it is possible to reach the last index of the array starting from the first index. The algorithm works by keeping track of the farthest index that can be reached (`f`). 

- **Key Observations:**
  1. If the farthest reachable index (`f`) becomes greater than or equal to the last index of the array, we return `True`.
  2. If at any point the farthest reachable index (`f`) stops progressing (i.e., we encounter a zero and cannot jump further), we return `False`.

- **Special Cases:**
  - If the array has only one element, you are already at the last index (`True`).
  - If the first element is `0` and the array has more than one element, you cannot move (`False`).

