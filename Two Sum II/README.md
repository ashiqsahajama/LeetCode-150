# LeetCode 167: Two Sum II - Input Array Is Sorted

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Return the indices of the two numbers as an array `[index1, index2]`, where `1 <= index1 < index2 <= numbers.length`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

### Constraints:
1. `2 <= numbers.length <= 3 * 10^4`
2. `-1000 <= numbers[i] <= 1000`
3. `numbers` is sorted in non-decreasing order.
4. `-1000 <= target <= 1000`
5. The tests are generated such that there is exactly one solution.

### Examples:

| Input                       | Output    |
|-----------------------------|-----------|
| `numbers = [2,7,11,15], target = 9` | `[1,2]`   |
| `numbers = [2,3,4], target = 6`     | `[1,3]`   |
| `numbers = [-1,0], target = -1`     | `[1,2]`   |

---

## Solution Explanation

This solution uses the **two-pointer technique** to efficiently find the two numbers that sum up to the target:

1. **Two Pointers**:
   - Initialize two pointers:
     - `i` at the start of the array.
     - `j` at the end of the array.

2. **Traverse the Array**:
   - Check the sum of `numbers[i]` and `numbers[j]`:
     - If the sum is less than `target`, move the left pointer `i` one step to the right to increase the sum.
     - If the sum is greater than `target`, move the right pointer `j` one step to the left to decrease the sum.
     - If the sum equals `target`, return `[i+1, j+1]`.

3. **Return Result**:
   - The result is guaranteed to exist, so the loop terminates when the target is found.

---
