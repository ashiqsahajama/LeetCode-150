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

### Solution for the 100% run time approach

# LeetCode 12: Integer to Roman

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/integer-to-roman/)

Given an integer, convert it to a Roman numeral. Roman numerals are represented by seven symbols: `I`, `V`, `X`, `L`, `C`, `D`, and `M`.

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

To represent numbers, Roman numerals use:
1. A combination of symbols added together (e.g., `III = 3`, `LVIII = 58`).
2. Subtractive combinations for specific cases:
   - `IV` = 4
   - `IX` = 9
   - `XL` = 40
   - `XC` = 90
   - `CD` = 400
   - `CM` = 900

Your task is to convert an integer `num` (1 ≤ num ≤ 3999) into its Roman numeral representation.

---

## Solution Explanation

This solution uses a **dictionary-based greedy approach** to map integer values to Roman numeral symbols.

1. **Symbol Mapping**:
   - Create a dictionary `d` where the keys are integer values (1000, 900, etc.) and the values are the corresponding Roman numeral symbols (`M`, `CM`, etc.).

2. **Iterative Conversion**:
   - For each key-value pair in the dictionary, subtract the key value from the input number `num` as many times as possible, appending the corresponding symbol to the result string `res`.

3. **Break Condition**:
   - Once `num` becomes 0, the loop stops, and the final Roman numeral string is returned.

---
