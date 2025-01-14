# LeetCode 30: Substring with Concatenation of All Words

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)

You are given a string `s` and an array of strings `words`. All the strings in `words` are of the same length. Return all starting indices of substrings in `s` that are a concatenation of each word in `words` exactly once, in any order, and without any intervening characters.

### Constraints:
1. `1 <= s.length <= 10^4`
2. `1 <= words.length <= 5000`
3. `1 <= words[i].length <= 30`
4. All words in `words` are of the same length.
5. `s` and `words[i]` consist of lowercase English letters.

### Examples:

| Input                                      | Output  |
|--------------------------------------------|---------|
| `s = "barfoothefoobarman", words = ["foo","bar"]` | `[0,9]` |
| `s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]` | `[]`     |
| `s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]` | `[6,9,12]` |

---

## Solution Explanation

This solution efficiently finds all starting indices of substrings in `s` that match the concatenation of all words in `words`:

1. **Preprocess `words`**:
   - Create a frequency dictionary (`main_dict`) to store the count of each word in `words`.

2. **Iterate Over Substrings**:
   - Define the length of the concatenated substring (`ite = len(words[0]) * len(words)`).
   - Slide a window of size `ite` across `s`.

3. **Validate Substring**:
   - For each starting index `i`, create a frequency dictionary (`dict2`) for the substring.
   - Divide the substring into chunks of size `len(words[0])` and count occurrences.
   - Compare `dict2` with `main_dict`. If they match, add `i` to the result list.

4. **Return Results**:
   - Return the list of all starting indices.

---
