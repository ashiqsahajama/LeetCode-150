# LeetCode 150 Solutions

## Table of Contents
- [Candy](LeetCode/Candy)

---

## Problem Explanations

### Candy

- **Problem:** [LeetCode Link](https://leetcode.com/problems/candy/)

  There are `n` children standing in a line, and each child is assigned a rating value given in the `ratings` array.

  You are tasked with distributing candies to these children under the following constraints:
  1. Each child must have at least one candy.
  2. Children with a higher rating than their immediate neighbors must get more candies than their neighbors.

  Return the minimum number of candies you need to distribute.

---

### Solution Explanation

This solution uses two passes to determine the minimum candies required:
1. **Left-to-Right Pass (`res_l`)**:
   - For each child, if their rating is greater than the previous child's, they get one more candy than the previous child.

2. **Right-to-Left Pass (`res_r`)**:
   - For each child, if their rating is greater than the next child's, they get one more candy than the next child.

3. **Combine Results**:
   - For each child, take the maximum candies required from the left-to-right and right-to-left passes to satisfy the conditions.
   - Sum up the candies for the final result.

---
