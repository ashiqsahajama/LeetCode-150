# LeetCode 151: Reverse Words in a String

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/reverse-words-in-a-string/)

Given an input string `s`, reverse the order of the words. Words are separated by spaces, and leading or trailing spaces should be removed. Additionally, ensure that multiple spaces between words are reduced to a single space.

### Constraints:
1. `1 <= len(s) <= 10^4`
2. `s` contains only printable ASCII characters.

### Examples:

| Input                                | Output                |
|--------------------------------------|-----------------------|
| `"the sky is blue"`                  | `"blue is sky the"`   |
| `"  hello world  "`                  | `"world hello"`       |
| `"a good   example"`                 | `"example good a"`    |

---

## Solution Explanation

This solution reverses the words in the string in a structured manner:

1. **Append Sentinel Character**:
   - Add a sentinel character (`"*"`) at the end of the string to simplify processing.

2. **Extract Words**:
   - Traverse the string, identifying alphanumeric characters to build individual words.
   - Append each word to a result list when a non-alphanumeric character (space or sentinel) is encountered.

3. **Reverse the Words**:
   - Reverse the order of the words in the result list.
   - Filter out any empty words caused by extra spaces.

4. **Join the Words**:
   - Join the reversed words with a single space to form the final output.

---
