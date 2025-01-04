# LeetCode 6: Zigzag Conversion

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/zigzag-conversion/)

The string `s` is written in a zigzag pattern on a given number of rows (`numRows`). The characters are then read row by row. Write a function to return this zigzag conversion.

### Constraints:
1. `1 <= s.length <= 1000`
2. `s` consists of English letters (lowercase and uppercase), digits, and symbols.
3. `1 <= numRows <= 1000`

### Examples:

| Input                                 | Output       |
|---------------------------------------|--------------|
| `"PAYPALISHIRING", numRows = 3`       | `"PAHNAPLSIIGYIR"` |
| `"PAYPALISHIRING", numRows = 4`       | `"PINALSIGYAHRPI"` |
| `"A", numRows = 1`                    | `"A"`        |

---

## Solution Explanation

This solution computes the zigzag conversion efficiently:

1. **Edge Case**:
   - If `numRows` is 1, the string remains unchanged as there is no zigzag pattern.

2. **Zigzag Pattern Construction**:
   - The zigzag pattern follows a cyclic pattern, with a full cycle length (`cycleLen`) of `(numRows - 1) * 2`.
   - Each row:
     - The first character is at index `r` (`0 ≤ r < numRows`).
     - Subsequent characters are at intervals of `cycleLen`.
     - Middle rows (`1 ≤ r < numRows - 1`) have an additional character in each cycle, at index `i + cycleLen - 2*r`.

3. **Traverse by Row**:
   - For each row, collect the corresponding characters based on the cyclic pattern.

4. **Concatenate Results**:
   - Combine all rows to form the final zigzag string.

---

