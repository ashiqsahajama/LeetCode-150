# LeetCode 68: Text Justification

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/text-justification/)

Given an array of strings `words` and an integer `maxWidth`, format the text such that each line has exactly `maxWidth` characters and is fully (left and right) justified.

- You should pack your words in a greedy manner; that is, pack as many words as possible in each line.
- Pad extra spaces `' '` when necessary so that each line has exactly `maxWidth` characters.
- Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the extra spaces are distributed starting from the left.

### Constraints:
1. `1 <= len(words) <= 300`
2. `1 <= len(words[i]) <= 20`
3. `maxWidth` is between 1 and 100.
4. `words[i]` consists only of English letters and symbols.

### Examples:

| Input                                             | Output                                 |
|---------------------------------------------------|----------------------------------------|
| `words = ["This", "is", "an", "example", "of", "text", "justification."]`, `maxWidth = 16` | `["This    is    an", "example  of text", "justification.  "]` |
| `words = ["What","must","be","acknowledgment","shall","be"]`, `maxWidth = 16`            | `["What   must   be", "acknowledgment  ", "shall be        "]` |

---

## Solution Explanation

This solution ensures full text justification by dividing the input words into lines, adding spaces as necessary, and handling edge cases for the last line.

### Steps:

1. **Greedy Line Packing**:
   - Accumulate words into a line until adding another word would exceed `maxWidth`.
   - Track the total length of characters in the line (`length`) and the number of words.

2. **Justify Each Line**:
   - Calculate the total spaces required (`maxWidth - length`).
   - For non-last lines:
     - Distribute spaces evenly between words.
     - Add extra spaces (if any) starting from the left.
   - For the last line:
     - Left-align words and pad spaces to the right.

3. **Construct Result**:
   - Add each justified line to the result list.
   - Ensure the last line is left-justified with remaining spaces added to the end.

---
