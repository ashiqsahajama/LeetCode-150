# LeetCode 205: Isomorphic Strings

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/isomorphic-strings/)

Given two strings `s` and `t`, determine if they are **isomorphic**. Two strings are isomorphic if the characters in `s` can be replaced to get `t`, ensuring:

1. Each character in `s` maps to a unique character in `t`.
2. No two characters in `s` map to the same character in `t`.

### Constraints:
1. \( 1 \leq s.length, t.length \leq 5 \times 10^4 \)
2. `s` and `t` consist of any printable ASCII characters.

### Examples:

| Input              | Output  |
|--------------------|---------|
| `s = "egg", t = "add"` | `True`  |
| `s = "foo", t = "bar"` | `False` |
| `s = "paper", t = "title"` | `True`  |

---

## Solution Explanation

This solution checks the isomorphism of two strings by maintaining two dictionaries:

1. **`has` Dictionary**:
   - Maps characters from `s` to `t`.

2. **`hat` Dictionary**:
   - Maps characters from `t` to `s`.

### Steps:

1. **Iterate through each character in the strings**:
   - Check if the character from `s` is already mapped to a different character in `t` (via `has` dictionary).
   - Check if the character from `t` is already mapped to a different character in `s` (via `hat` dictionary).

2. **Mapping Validation**:
   - If inconsistent mapping is found, return `False`.
   - Otherwise, update both mappings.

3. **Return Result**:
   - If no conflicting mappings are found, return `True`.

---

## Code

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        has = {}
        hat = {}

        for i in range(len(s)):
            a = s[i]
            b = t[i]
            if ((a in has and has[a] != b) or  
                (b in hat and hat[b] != a)):
                return False
            has[a] = b
            hat[b] = a

        return True
