# LeetCode 125: Valid Palindrome

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/valid-palindrome/)

Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

### Constraints:
1. `1 <= len(s) <= 2 * 10^5`
2. `s` consists only of printable ASCII characters.

### Examples:

| Input                                   | Output |
|-----------------------------------------|--------|
| `"A man, a plan, a canal: Panama"`      | `True` |
| `"race a car"`                          | `False`|
| `" "`                                   | `True` |

---

## Solution Explanation

This solution uses a two-pointer approach to efficiently determine if the given string is a palindrome:

1. **Initialization**:
   - Use two pointers, `i` starting at the beginning and `j` at the end of the string.
   - Assume the string is a palindrome until proven otherwise.

2. **Two-Pointer Traversal**:
   - Compare the characters at `i` and `j`, ignoring case differences:
     - If both characters are alphanumeric and match, move both pointers inward.
     - If `s[i]` is not alphanumeric, move the `i` pointer forward.
     - If `s[j]` is not alphanumeric, move the `j` pointer backward.
     - If the characters do not match, return `False`.

3. **Edge Case**:
   - If the string is empty or contains only non-alphanumeric characters, it is considered a palindrome.

4. **Return Result**:
   - If all characters match or are skipped correctly, return `True`.

---
