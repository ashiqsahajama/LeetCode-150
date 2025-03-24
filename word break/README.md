# LeetCode 139: Word Break

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/word-break/)

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

Note that the **same word** in the dictionary may be reused multiple times in the segmentation.

### Constraints:
1. `1 <= s.length <= 10^4`
2. `1 <= wordDict.length <= 1000`
3. `1 <= wordDict[i].length <= 20`
4. `s` and `wordDict[i]` consist of only lowercase English letters.
5. All the strings in `wordDict` are unique.

### Examples:

| Input                        | Output | Explanation                              |
|-----------------------------|--------|------------------------------------------|
| `s = "leetcode"` <br> `wordDict = ["leet", "code"]` | `true`  | `"leetcode"` = `"leet"` + `"code"`       |
| `s = "applepenapple"` <br> `wordDict = ["apple", "pen"]` | `true`  | `"applepenapple"` = `"apple"` + `"pen"` + `"apple"` |
| `s = "catsandog"` <br> `wordDict = ["cats", "dog", "sand", "and", "cat"]` | `false` | Cannot be segmented into dictionary words |

---

## Solution Explanation

This problem is solved using **Dynamic Programming** with bottom-up approach:

1. **DP Array**:
   - Create a boolean array `dp` of length `len(s) + 1`, where `dp[i]` represents whether the substring `s[i:]` can be segmented using words from `wordDict`.
   - Initialize `dp[len(s)] = True`, meaning an empty string can always be segmented.

2. **Iterate Backwards**:
   - Traverse the string `s` from the end to the beginning.
   - For each index `i`, check every word `w` in `wordDict`:
     - If `s[i:i+len(w)] == w`, then check if `dp[i+len(w)]` is `True`.
     - If it is, set `dp[i] = True` and break early.

3. **Final Output**:
   - Return `dp[0]`, which tells whether the whole string `s` can be segmented.

---

## Code

```python
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]
