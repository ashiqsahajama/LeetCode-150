# LeetCode 36: Valid Sudoku

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/valid-sudoku/)

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

### Constraints:
1. The board is a `9 x 9` array.
2. Each element is a digit `'1'-'9'` or a `'.'` to represent an empty cell.

### Examples:

| Input                                                                 | Output  |
|-----------------------------------------------------------------------|---------|
| `[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]` | `True`  |
| `[["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]` | `False` |

---

## Solution Explanation

This solution validates the Sudoku board by keeping track of:
1. **Rows**: Ensures no duplicate digits in each row.
2. **Columns**: Ensures no duplicate digits in each column.
3. **Boxes**: Ensures no duplicate digits in each `3 x 3` sub-box.

### Steps:

1. **Initialize Data Structures**:
   - Use dictionaries with sets to store seen digits for rows, columns, and boxes.

2. **Traverse the Board**:
   - For each cell `(i, j)`:
     - Skip empty cells (`.`).
     - Check if the digit already exists in the corresponding row, column, or box.
     - If a duplicate is found, return `False`.

3. **Add to Sets**:
   - Add the digit to the respective row, column, and box sets.

4. **Return Result**:
   - If all cells are validated without conflicts, return `True`.

---
