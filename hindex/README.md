# LeetCode 150 Solutions

## Table of Contents
- [H-Index](LeetCode/HIndex)

---

## Problem Explanations

### H-Index

- **Problem:** [LeetCode Link](https://leetcode.com/problems/h-index/)

  Given an array `citations` where `citations[i]` represents the number of citations a researcher has received for their `i`th paper, return the researcher's H-Index.

  The H-Index is defined as the maximum value `h` such that the researcher has at least `h` papers with `h` or more citations, and the other papers have no more than `h` citations.

---

### Solution Explanation

The solution sorts the `citations` array in descending order and iteratively calculates the H-Index:

1. **Sorting**:
   - Sort the citations array in descending order so that the most cited papers come first.
   
2. **H-Index Calculation**:
   - Traverse the sorted array and increment the H-Index (`h`) as long as the current citation count is greater than or equal to `h + 1`.
   - The loop stops when this condition is no longer satisfied, and the current value of `h` is returned.
  
   - The base idea is to find h such that there are items in array such that they are greater than h and the remaining elements in the array values should be less than h.
   - So sort the array and start from the largest index in the sorted array, increment h if current index is greater than h because the largest element will have atleast h for sure.
   - If the condition is met then increment h and check if next index is greater or equal to h+1.



