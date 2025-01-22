# LeetCode 290: Word Pattern

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/word-pattern/)

Given a pattern string `pattern` and a space-separated string `s`, determine if `s` follows the same pattern as `pattern`.

A string `s` follows a pattern if there is a **bijective mapping** (one-to-one correspondence) between a character in `pattern` and a word in `s`.

### Constraints:
1. \( 1 \leq \text{pattern.length} \leq 300 \)
2. `s` consists of lowercase English letters and spaces.
3. `s` does not contain leading or trailing spaces.
4. `s` contains at least one word.

### Examples:

| Input                            | Output  |
|----------------------------------|---------|
| `pattern = "abba", s = "dog cat cat dog"` | `True`  |
| `pattern = "abba", s = "dog cat cat fish"` | `False` |
| `pattern = "aaaa", s = "dog cat cat dog"` | `False` |
| `pattern = "abba", s = "dog dog dog dog"` | `False` |

---

## Solution Explanation

This solution checks if the given pattern and words in `s` follow a one-to-one mapping by using two dictionaries:

1. **Preprocessing**:
   - Split the string `s` into words using the `split()` function.

2. **Edge Case Check**:
   - If the number of words in `s` is not equal to the length of `pattern`, return `False`.

3. **Mapping Validation**:
   - Iterate through each character-word pair in `pattern` and `s`.
   - Use two dictionaries:
     - `chk1` to map words to pattern characters.
     - `chk2` to map pattern characters to words.
   - Check if either mapping is inconsistent:
     - If a mapping exists but does not match the current character or word, return `False`.

4. **Return Result**:
   - If all mappings are valid, return `True`.

---

## Code

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        chk1 = {}
        chk2 = {}

        if len(s) != len(pattern):
            return False

        for i in range(len(s)):
            a = s[i]
            b = pattern[i]
            if ((a in chk1 and chk1[a] != b) or (b in chk2 and chk2[b] != a)):
                 return False
            chk1[a] = b
            chk2[b] = a
        
        return True
