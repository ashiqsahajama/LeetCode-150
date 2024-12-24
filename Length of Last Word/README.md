# LeetCode 58: Length of Last Word

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/length-of-last-word/)

Given a string `s` consisting of words and spaces, return the length of the last word in the string. A word is defined as a contiguous sequence of non-space characters.

### Constraints:
1. `1 <= len(s) <= 10^4`
2. `s` contains only English letters and spaces `' '`.
3. There will always be at least one word in `s`.

### Examples:

| Input                   | Output |
|--------------------------|--------|
| `"Hello World"`          | 5      |
| `"   fly me   to   the moon  "` | 4      |
| `"luffy is still joyboy"`| 6      |

---

## Solution Explanation

This solution processes the string from the end to determine the length of the last word:

1. **Strip Trailing Spaces**:
   - Traverse the string from the end to remove any trailing spaces.
   - Once a non-space character is found, stop trimming.

2. **Count the Characters of the Last Word**:
   - Iterate backward from the last character of the trimmed string.
   - Count all contiguous alphabetic characters until a space is encountered.

3. **Return the Length**:
   - Return the count as the length of the last word.

### Example Walkthrough:

Input: `"   fly me   to   the moon  "`

1. Remove trailing spaces: `"   fly me   to   the moon"`
2. Count characters in the last word (`"moon"`): `4`
3. Return `4`.

---

## Solution 2 Explanation

This solution efficiently finds the length of the last word by using two pointers:

1. **Remove Trailing Spaces**:
   - Start from the last character of the string and move backward to skip trailing spaces.

2. **Find the Last Word**:
   - Use another pointer to traverse backward until a space is encountered or the start of the string is reached.
   - The difference between the two pointers gives the length of the last word.

### Example Walkthrough:

Input: `"   fly me   to   the moon  "`

1. Start from the last character (`j = 28`) and skip trailing spaces:
   - `j = 23`, pointing to `'n'`.
2. Traverse backward to find the last word:
   - `i = 20`, pointing to `' '`.
3. Length of the last word: `j - i = 23 - 20 = 4`.

---
