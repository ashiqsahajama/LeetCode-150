# LeetCode 150 Solutions

## Table of Contents
- [Jump Game II](LeetCode/JumpGameII)

---

## Problem Explanations

### Jump Game II

- **Problem:** [LeetCode Link](https://leetcode.com/problems/jump-game-ii/)

  You are given an integer array `nums` where `nums[i]` represents the maximum number of steps you can jump forward from that position. 

  Your goal is to reach the last index in the minimum number of jumps. Return the minimum number of jumps required to reach the last index.

---

### Solution Explanation

The solution uses a **Greedy Algorithm** to calculate the minimum number of jumps required to reach the last index. 

- **Key Observations:**
  1. At each step, calculate the farthest index (`max_reach`) that can be reached from the current position.
  2. Use a variable `limit` to track the end of the current "range" or "level" of jumps. Each time we exceed this limit, increment the jump counter and update the limit to the current `max_reach`.
  3. Continue this process until we reach or exceed the last index.

