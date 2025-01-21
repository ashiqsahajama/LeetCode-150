# LeetCode 383: Ransom Note

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/ransom-note/)

Given two strings `ransomNote` and `magazine`, return `True` if `ransomNote` can be constructed from `magazine` and `False` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

### Constraints:
1. \( 1 \leq \text{ransomNote.length}, \text{magazine.length} \leq 10^5 \)
2. `ransomNote` and `magazine` consist of lowercase English letters.

### Examples:

| Input                         | Output  |
|-------------------------------|---------|
| `ransomNote = "a", magazine = "b"` | `False` |
| `ransomNote = "aa", magazine = "ab"` | `False` |
| `ransomNote = "aa", magazine = "aab"` | `True`  |

---

## Solution Explanation

This solution uses a frequency count to check if `ransomNote` can be formed using letters from `magazine`:

1. **Count Letter Frequencies**:
   - Use Python's `Counter` from the `collections` module to count occurrences of each letter in `magazine`.

2. **Check Letter Availability**:
   - Iterate through each letter in `ransomNote` and check if it exists in the `Counter` with a count greater than zero.
   - If a letter is not available or its count reaches zero, return `False`.
   - Otherwise, decrement the letter count in the `Counter`.

3. **Return Result**:
   - If all letters are satisfied, return `True`.

---

## Code

```python
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        has = Counter(magazine)

        for i in ransomNote:
            if i not in has or has[i] <= 0:
                return False
            has[i] -= 1
            
        return True
