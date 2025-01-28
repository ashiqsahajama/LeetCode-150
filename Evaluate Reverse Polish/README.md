# LeetCode 150: Evaluate Reverse Polish Notation

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

You are given an array of strings `tokens` that represents an expression in **Reverse Polish Notation** (RPN). Evaluate the expression and return its value.

Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression. Division between two integers should truncate toward zero.

### Constraints:
1. \( 1 \leq \text{tokens.length} \leq 10^4 \)
2. `tokens[i]` is one of `+`, `-`, `*`, `/`, or an integer in the range \([-200, 200]\).
3. The input is guaranteed to be a valid RPN expression.
4. The division result is always an integer.

### Examples:

| Input                                   | Output |
|-----------------------------------------|--------|
| `tokens = ["2","1","+","3","*"]`        | `9`    |
| `tokens = ["4","13","5","/","+"]`       | `6`    |
| `tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]` | `22` |


---

## Solution Explanation

This solution evaluates an RPN expression using a **stack-based approach**:

### Steps:

1. **Initialize a Stack**:
   - Use a stack to store intermediate results.

2. **Process Tokens**:
   - If the token is an operand (integer), push it onto the stack.
   - If the token is an operator (`+`, `-`, `*`, `/`):
     - Pop the top two elements from the stack.
     - Perform the operation using these two elements (`a` and `b`).
       - `b` is the second popped element (the top of the stack).
       - `a` is the first popped element.
     - Push the result back onto the stack.

3. **Handle Division**:
   - Use `int(a / b)` for division to ensure truncation toward zero.

4. **Return the Result**:
   - The result is the last element left in the stack.

---

## Code

```python
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i not in ['+', '-', '*', '/']:
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                if i == "+":
                    stack.append(a + b)
                elif i == "-":
                    stack.append(a - b)
                elif i == "*":
                    stack.append(a * b)
                elif i == "/":
                    stack.append(int(a / b))  # Truncate toward zero
        
        return stack[-1]


