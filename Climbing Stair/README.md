# LeetCode 70: Climbing Stairs

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/climbing-stairs/)

You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

### Constraints:
1. `1 <= n <= 45`

### Examples:

| Input  | Output |
|--------|--------|
| `n = 2` | `2` (1+1, 2) |
| `n = 3` | `3` (1+1+1, 1+2, 2+1) |
| `n = 4` | `5` (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2) |

---

## Solution Explanation

This problem follows the **Fibonacci sequence** pattern:

1. **Base Cases**:
   - If `n = 1`, there is only `1` way to climb.
   - If `n = 2`, there are `2` ways to climb.

2. **Iterative Approach**:
   - Use two variables (`prev` and `bef`) to store the number of ways to climb the previous two steps.
   - Start from `n = 3` and iterate up to `n`, computing the current number of ways as `curr = prev + bef`.
   - Update `bef` and `prev` accordingly.

3. **Final Output**:
   - The last computed value (`curr`) is the answer.

---

## Code

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev = 2
        bef = 1
        for i in range(2, n):
            curr = prev + bef
            bef = prev
            prev = curr
        return curr
