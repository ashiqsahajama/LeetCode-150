# LeetCode 9: Palindrome Number

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/palindrome-number/)

Given an integer `x`, return `true` if `x` is a **palindrome integer**.

A **palindrome number** reads the **same forward and backward**.

### Constraints:
1. \( -2^{31} \leq x \leq 2^{31} - 1 \)

---

## Solution Explanation

This solution **reverses the integer** and checks if it equals the original number.

### Steps:

1. **Negative Numbers are Not Palindromes**:
   - If `x < 0`, return `False`.

2. **Reverse the Number**:
   - Use modulo (`%`) to extract the last digit.
   - Build the reversed number (`b`) by multiplying the previous `b` by 10 and adding the extracted digit.
   - Continue until all digits are reversed.

3. **Compare Reversed Number with `x`**:
   - If `b == x`, return `True`; otherwise, return `False`.

Since `121 == 121`, return `True`.

For `x = -121`:
- Negative numbers are **not palindromes** → Return `False`.

---

## Code

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False  # Negative numbers are not palindromes

        a = x
        b = 0

        while a > 0:
            c = a % 10  # Extract last digit
            b = b * 10 + c  # Append digit to reversed number
            a //= 10  # Remove last digit

        return b == x  # Check if reversed number matches original


