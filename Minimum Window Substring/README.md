# LeetCode 76: Minimum Window Substring

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/minimum-window-substring/)

Given two strings `s` and `t` of lengths `m` and `n`, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If no such substring exists, return an empty string `""`.

### Constraints:
1. \( m, n \leq 10^5 \)
2. `s` and `t` consist of uppercase and lowercase English letters.

### Examples:

| Input                     | Output  |
|---------------------------|---------|
| `s = "ADOBECODEBANC", t = "ABC"` | `"BANC"` |
| `s = "a", t = "a"`         | `"a"`   |
| `s = "a", t = "aa"`        | `""`    |

---

## Solution Explanation

This solution uses the **sliding window technique** with two pointers and frequency dictionaries to find the minimum window substring:

1. **Frequency Map for `t`**:
   - Count the frequency of each character in `t` using a dictionary (`countT`).

2. **Sliding Window**:
   - Use two pointers (`l` and `r`) to represent the current window in `s`.
   - Maintain a frequency dictionary (`window`) for the current window.

3. **Check for Valid Window**:
   - Keep a variable `have` to track how many characters from `t` are fully satisfied in the current window.
   - Compare `have` with `need` (the total unique characters in `t`).

4. **Shrink the Window**:
   - When all characters in `t` are satisfied in the current window (`have == need`):
     - Update the result if the current window is smaller than the previously found minimum.
     - Shrink the window by moving the left pointer (`l`).

5. **Return Result**:
   - Return the substring corresponding to the smallest window if found, otherwise return an empty string.

---


