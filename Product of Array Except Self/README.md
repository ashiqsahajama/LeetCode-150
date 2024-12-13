# LeetCode 150 Solutions

## Table of Contents
- [Product of Array Except Self](LeetCode/ProductOfArrayExceptSelf)

---

## Problem Explanations

### Product of Array Except Self

- **Problem:** [LeetCode Link](https://leetcode.com/problems/product-of-array-except-self/)

  Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

  The solution must work **without using division** and in **O(n)** time complexity.

---

### Solution Explanation

This solution calculates the product of the array except for the current index (`nums[i]`) using two auxiliary arrays:
1. **Prefix Product Array (`pre`)**:
   - This array contains the product of all elements to the left of the current index.
2. **Suffix Product Array (`suf`)**:
   - This array contains the product of all elements to the right of the current index.

#### Steps:
1. **Calculate Prefix Products**:
   - Iterate from left to right and calculate the cumulative product of all elements to the left of each index.
2. **Calculate Suffix Products**:
   - Iterate from right to left and calculate the cumulative product of all elements to the right of each index.
3. **Combine Prefix and Suffix Products**:
   - For each index `i`, the result is the product of the prefix product at `i` and the suffix product at `i`.

