# LeetCode 28: Implement `strStr()`

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/implement-strstr/)

Implement the function `strStr(haystack: str, needle: str) -> int`, which finds the first occurrence of the string `needle` in the string `haystack`. If `needle` is not a substring of `haystack`, return `-1`.

### Constraints:
1. `1 <= haystack.length, needle.length <= 10^4`
2. `haystack` and `needle` consist of only lowercase English letters.

### Examples:

| Input                          | Output |
|--------------------------------|--------|
| `"hello", "ll"`                | `2`    |
| `"aaaaa", "bba"`               | `-1`   |
| `"", ""`                       | `0`    |

---

## Solution Explanation

This solution uses a straightforward sliding window approach:

1. **Edge Case**:
   - If `needle` is an empty string, the index `0` is returned, as per the problem description.

2. **Sliding Window**:
   - Calculate the length of `needle` (`m`).
   - Traverse the `haystack` using a loop, creating a substring of length `m` starting at each index.
   - Compare the substring with `needle`:
     - If they match, return the current index.
     - Otherwise, continue to the next index.

3. **Return -1**:
   - If the loop completes without finding `needle`, return `-1`.

### Example Walkthrough:

Input: `"hello", "ll"`

1. `needle` length: `m = 2`.
2. Traverse `haystack`:
   - At index `0`: Substring is `"he"` → No match.
   - At index `1`: Substring is `"el"` → No match.
   - At index `2`: Substring is `"ll"` → Match found, return `2`.

Output: `2`.
