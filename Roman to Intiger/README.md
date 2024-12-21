# LeetCode 150 Solutions

## Table of Contents
- [Roman to Integer](LeetCode/RomanToInteger)

---

## Problem Explanations

### Roman to Integer

- **Problem:** [LeetCode Link](https://leetcode.com/problems/roman-to-integer/)

  Roman numerals are represented by seven symbols: `I`, `V`, `X`, `L`, `C`, `D`, and `M`. Each symbol has a specific value:

  | Symbol | Value |
  |--------|-------|
  | I      | 1     |
  | V      | 5     |
  | X      | 10    |
  | L      | 50    |
  | C      | 100   |
  | D      | 500   |
  | M      | 1000  |

  Certain combinations of symbols represent specific values, such as:
  - `IV` = 4
  - `IX` = 9
  - `XL` = 40
  - `XC` = 90
  - `CD` = 400
  - `CM` = 900

  Given a Roman numeral string `s`, convert it to an integer.

---

### Solution Explanation

This solution processes the Roman numeral string using a **dictionary-based approach** and handles special cases for subtractive combinations (e.g., `IV`, `IX`).

1. **Symbol Mapping**:
   - Create a dictionary `d` to store the integer values for Roman numeral symbols.

2. **Traverse the String**:
   - Use a `while` loop to iterate through the string.
   - Check if the current symbol and the next symbol form a subtractive combination (e.g., `IV`, `IX`).
     - If they do, add the corresponding value to the result and skip the next symbol by incrementing the pointer by 2.
     - Otherwise, add the value of the current symbol to the result and move to the next symbol.

3. **Handle Last Symbol**:
   - If the loop ends with one unprocessed symbol (when the string length is odd), add its value to the result.

4. **Return Result**:
   - Return the computed integer value.

---
