# LeetCode 392: Is Subsequence

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/is-subsequence/)

Given two strings `s` and `t`, check if `s` is a subsequence of `t`.

A subsequence of a string is a new string generated from the original string by deleting some or no characters without changing the relative order of the remaining characters.

### Constraints:
1. `0 <= s.length <= 100`
2. `0 <= t.length <= 10^4`
3. `s` and `t` consist only of lowercase English letters.

### Examples:

| Input                       | Output |
|-----------------------------|--------|
| `s = "abc", t = "ahbgdc"`   | `True` |
| `s = "axc", t = "ahbgdc"`   | `False`|

---

## Solution Explanation

This solution determines if `s` is a subsequence of `t` by:

1. **Concatenating `s`, a separator, and `t`**:
   - Create a combined string `a = s + "*" + t` to traverse both `s` and `t` in a single pass.

2. **Two-Pointer Technique**:
   - Use two pointers:
     - `i` to traverse `s`.
     - `j` to traverse `t` (offset by the length of `s` + 1 to skip over `s` and the separator).
   - Compare characters of `s` and `t`:
     - If characters match, move both pointers forward.
     - Otherwise, move the pointer for `t` only.

3. **Construct Subsequence**:
   - Build a string `b` using the matched characters from `s` and `t`.

4. **Final Check**:
   - Compare `b` with `s`. If they are equal, `s` is a subsequence of `t`.

---
