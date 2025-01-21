# LeetCode 73: Set Matrix Zeroes

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/set-matrix-zeroes/)

Given an `m x n` integer matrix, if an element is `0`, set its entire row and column to `0` in-place.

### Constraints:
1. \( m == \text{matrix.length} \)
2. \( n == \text{matrix[0].length} \)
3. \( 1 \leq m, n \leq 200 \)
4. \(-2^{31} \leq \text{matrix[i][j]} \leq 2^{31} - 1 \)

### Examples:

| Input                                    | Output                                     |
|------------------------------------------|--------------------------------------------|
| `[[1,1,1],[1,0,1],[1,1,1]]`              | `[[1,0,1],[0,0,0],[1,0,1]]`                |
| `[[0,1,2,0],[3,4,5,2],[1,3,1,5]]`        | `[[0,0,0,0],[0,4,5,0],[0,3,1,0]]`          |

---

## Solution Explanation

This solution efficiently marks the rows and columns to be zeroed using the first row and first column as flags:

1. **Identify Zero Positions**:
   - Iterate through the matrix.
   - If an element is `0`, mark its row and column using the first row and column.
   - Use a boolean flag `rowZero` to track if the first row should be zeroed.

2. **Update Matrix Based on Flags**:
   - Traverse the matrix starting from index `(1,1)` and set elements to `0` based on the markers set earlier.

3. **Handle First Row and Column Separately**:
   - If the first cell (`matrix[0][0]`) is `0`, set the entire first column to zero.
   - If `rowZero` is `True`, set the entire first row to zero.

---

## Code

```python
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        rowZero = False

        # Mark the first row and first column to identify rows and columns to be zeroed
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0  # Mark column
                    if r > 0:
                        matrix[r][0] = 0  # Mark row
                    else:
                        rowZero = True  # Track if the first row should be zeroed

        # Set matrix elements to zero based on markers
        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Handle first column separately
        if matrix[0][0] == 0:
            for r in range(row):
                matrix[r][0] = 0

        # Handle first row separately if required
        if rowZero:
            for c in range(col):
                matrix[0][c] = 0
