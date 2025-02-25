# LeetCode 74: Search a 2D Matrix

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/search-a-2d-matrix/)

You are given an `m x n` matrix where:
- Each row is sorted in **ascending order**.
- The **first integer of each row is greater** than the last integer of the previous row.

Given a target integer, return `True` if it exists in the matrix, otherwise return `False`.

### Constraints:
1. \( m == \text{matrix.length} \)
2. \( n == \text{matrix[0].length} \)
3. \( 1 \leq m, n \leq 100 \)
4. \( -10^4 \leq \text{matrix[i][j]}, \text{target} \leq 10^4 \)

---

## Solution Explanation

This solution **flattens the 2D matrix into a 1D array** and applies **binary search** efficiently.

### Steps:

1. **Convert 2D Index to 1D**:
   - Treat the matrix as a **1D sorted list**.
   - Compute `mid_r = mid // c` (row index).
   - Compute `mid_c = mid % c` (column index).

2. **Apply Binary Search**:
   - Compute `mid = (l + r) // 2` (midpoint).
   - If `matrix[mid_r][mid_c] == target`, return `True`.
   - If `matrix[mid_r][mid_c] < target`, search **right** (`l = mid + 1`).
   - If `matrix[mid_r][mid_c] > target`, search **left** (`r = mid - 1`).

3. **Return `False` if Not Found**.

---

## Code

```python
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = (rows * cols) - 1  # Flattened search space

        while l <= r:
            mid = (l + r) // 2
            mid_r = mid // cols  # Compute row index
            mid_c = mid % cols   # Compute column index

            if matrix[mid_r][mid_c] == target:
                return True
            elif matrix[mid_r][mid_c] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
