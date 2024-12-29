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

Given an input string `s`, reverse the order of the words. Words are separated by spaces, and leading or trailing spaces should be removed. Additionally, multiple spaces between words should be reduced to a single space in the final output.

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

This solution uses Python's built-in string and list methods for simplicity:

1. **Split the String**:
   - Use `split()` to split the string into a list of words, automatically removing extra spaces.

2. **Reverse the List**:
   - Use slicing (`[::-1]`) to reverse the order of the words in the list.

3. **Join the Words**:
   - Use `join()` to combine the words in the reversed list into a single string, separated by a single space.

---

## Code

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()  # Split the string into words and remove extra spaces
        s = s[::-1]    # Reverse the list of words
        return " ".join(s)  # Join the words with a single space
