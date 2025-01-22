# LeetCode 49: Group Anagrams

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/group-anagrams/)

Given an array of strings `strs`, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Constraints:
1. \( 1 \leq \text{strs.length} \leq 10^4 \)
2. \( 0 \leq \text{strs[i].length} \leq 100 \)
3. `strs[i]` consists of lowercase English letters.

### Examples:

| Input                                 | Output                                      |
|---------------------------------------|---------------------------------------------|
| `["eat","tea","tan","ate","nat","bat"]` | `[["bat"],["nat","tan"],["ate","eat","tea"]]` |
| `[""]`                                | `[[""]]`                                    |
| `["a"]`                               | `[["a"]]`                                   |

---

## Solution Explanation

This solution groups anagrams by counting the frequency of each character in the strings and using the counts as keys to group words:

1. **Initialize Data Structures**:
   - Use a dictionary (`defaultdict(list)`) to store groups of anagrams.

2. **Character Frequency Counting**:
   - For each string in `strs`:
     - Create an array `count` of size 26 to store the frequency of each character (since only lowercase letters are considered).
     - Convert the count array to a tuple (hashable) and use it as a key in the dictionary to group anagrams.

3. **Collect Results**:
   - Convert dictionary values to a list of lists and return the grouped anagrams.

---

## Code

```python
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r = defaultdict(list)

        for i in strs:
            count = [0] * 26  # Array to count character occurrences
            for j in i:
                count[ord(j) - ord('a')] += 1  # Convert character to index
            
            r[tuple(count)].append(i)  # Store words with the same count signature

        return list(r.values())
