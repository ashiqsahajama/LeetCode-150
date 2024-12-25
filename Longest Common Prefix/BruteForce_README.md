# LeetCode 14: Longest Common Prefix

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/longest-common-prefix/)

Given an array of strings `strs`, find the longest common prefix among all strings. If no common prefix exists, return an empty string `""`.

### Constraints:
1. `1 <= strs.length <= 200`
2. `0 <= strs[i].length <= 200`
3. `strs[i]` consists of only lowercase English letters.

### Examples:

| Input                         | Output      |
|-------------------------------|-------------|
| `["flower","flow","flight"]`  | `"fl"`      |
| `["dog","racecar","car"]`     | `""`        |
| `[""]`                        | `""`        |
| `["a"]`                       | `"a"`       |

---

## Solution Explanation

This solution determines the longest common prefix in a step-by-step manner:

1. **Base Cases**:
   - If the input list contains only one string, return that string.
   - If the list contains two strings, find their common prefix directly.

2. **Two-String Comparison**:
   - Compare characters in the first two strings up to the length of the shorter string.
   - Build a prefix `c` by appending matching characters until a mismatch is found.

3. **Iterative Comparison**:
   - For the remaining strings in the list, compare each one with the current common prefix.
   - Update the prefix by keeping only the characters that match.

4. **Final Result**:
   - If a prefix remains after comparing all strings, return it.
   - If no common prefix exists, return `""`.

---

