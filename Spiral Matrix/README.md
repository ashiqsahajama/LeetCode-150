# LeetCode 54: Spiral Matrix

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/spiral-matrix/)

Given an \( m \times n \) matrix, return all elements of the matrix in spiral order.

### Constraints:
1. \( m == \text{matrix.length} \)
2. \( n == \text{matrix[0].length} \)
3. \( 1 \leq m, n \leq 10 \)
4. \(-100 \leq \text{matrix[i][j]} \leq 100 \)

### Examples:

| Input                                 | Output               |
|---------------------------------------|----------------------|
| `[[1,2,3],[4,5,6],[7,8,9]]`           | `[1,2,3,6,9,8,7,4,5]`|
| `[[1,2,3,4],[5,6,7,8],[9,10,11,12]]`  | `[1,2,3,4,8,12,11,10,9,5,6,7]` |

---

## Solution Explanation

This solution traverses the matrix in a spiral order by iteratively updating the boundaries of the traversal:

1. **Initialize Boundaries**:
   - `top`: Tracks the top row.
   - `bottom`: Tracks the bottom row.
   - `left`: Tracks the left column.
   - `right`: Tracks the right column.

2. **Traverse the Matrix**:
   - Move **left to right** along the `top` row.
   - Move **top to bottom** along the `right` column.
   - Check if boundaries overlap. If not:
     - Move **right to left** along the `bottom` row.
     - Move **bottom to top** along the `left` column.

3. **Adjust Boundaries**:
   - After each traversal, update the boundaries (`top`, `bottom`, `left`, `right`) to move inward.

4. **Break Condition**:
   - Stop when the `top` boundary meets or exceeds `bottom` or when the `left` boundary meets or exceeds `right`.

5. **Return Result**:
   - Collect elements in spiral order and return the result.

---
