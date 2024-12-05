# LeetCode 150 Solutions

## Table of Contents
- [Merge Sorted Array](LeetCode/MergeSortedArray)

---

## Problem Explanations

### Merge Sorted Array

- **Problem:** [LeetCode Link](https://leetcode.com/problems/merge-sorted-array/)

  You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order. Initially, `nums1` has enough space (size = `m + n`) to hold all the elements from `nums2`. The first `m` elements of `nums1` represent the elements that need to be merged, and the last `n` elements are initialized to zero and should be ignored. The `nums2` array has `n` elements. 

  **Objective**: Merge the two arrays into one sorted array in **non-decreasing** order, modifying `nums1` in-place.

- **Solution Explanation:**
  - The solution uses a two-pointer technique to merge the two sorted arrays.
  - We start from the end of both arrays (`nums1` and `nums2`) and compare the elements.
  - The larger element is placed in the last position of `nums1`, and the corresponding pointer (`a` for `nums1` and `b` for `nums2`) is decremented.
  - This process continues until all elements from `nums2` are merged into `nums1`. If there are any remaining elements in `nums1` (which will already be sorted), they remain in place.

---
