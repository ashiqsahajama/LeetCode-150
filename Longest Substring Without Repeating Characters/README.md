# LeetCode 3: Longest Substring Without Repeating Characters

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Given a string `s`, find the length of the longest substring without repeating characters.

### Constraints:
1. \( 0 \leq s.length \leq 5 \times 10^4 \)
2. \( s \) consists of English letters, digits, symbols, and spaces.

### Examples:

| Input             | Output |
|-------------------|--------|
| `"abcabcbb"`      | `3`    |
| `"bbbbb"`         | `1`    |
| `"pwwkew"`        | `3`    |
| `""`              | `0`    |

---

## Solution Explanation

This solution uses the **sliding window technique** with a hash set to efficiently find the longest substring without repeating characters:

1. **Initialize Variables**:
   - `res`: A hash set to store unique characters in the current substring.
   - `m`: Tracks the maximum length of the substring found so far.
   - `l`: Left pointer of the sliding window.

2. **Iterate Through the String**:
   - Use the right pointer `i` to traverse the string.
   - If `s[i]` is already in the set:
     - Remove characters starting from the left pointer `l` until `s[i]` is removed.
     - Increment the left pointer `l` for each removal.
   - Add `s[i]` to the set and update `m` with the maximum length of the current substring (`i - l + 1`).

3. **Return Result**:
   - After processing the string, return `m`, which contains the length of the longest substring without repeating characters.

---
