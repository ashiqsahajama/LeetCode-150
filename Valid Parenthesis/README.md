# LeetCode 20: Valid Parentheses

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/valid-parentheses/)

Given a string `s` containing just the characters `'(', ')', '{', '}', '[' and ']'`, determine if the input string is valid.

A string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### Constraints:
1. \( 1 \leq \text{len}(s) \leq 10^4 \)
2. `s` consists of parentheses characters only.

### Examples:

| Input           | Output |
|-----------------|--------|
| `s = "()"`      | `True`  |
| `s = "()[]{}"`  | `True`  |
| `s = "(]"`      | `False` |
| `s = "([)]"`    | `False` |
| `s = "{[]}"`    | `True`  |

---

## Solution Explanation

This solution checks for valid parentheses using a **stack-based approach**:

### Steps:

1. **Edge Case Check**:
   - If the length of `s` is odd, return `False` (since valid parentheses require pairs).

2. **Initialize a Stack**:
   - Use a stack to track open parentheses.

3. **Process Each Character**:
   - If the character is an opening bracket, push it onto the stack.
   - If it's a closing bracket:
     - Check if the stack is non-empty and the top of the stack matches the corresponding opening bracket.
     - If valid, pop the stack.
     - If not, return `False`.

4. **Final Check**:
   - If the stack is empty after processing all characters, the string is valid; otherwise, it's invalid.

---

## Code

```python
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        hash = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        
        for i in s:
            if i in hash.values():  # If it's an opening bracket
                stack.append(i)
            elif len(stack) >= 1 and stack[-1] == hash[i]:  # If it's a matching closing bracket
                stack.pop()
            else:
                return False
        
        return not stack  # Returns True if the stack is empty
