
---

## Solution Explanation

This solution determines if a number is happy using the following approach:

1. **Helper Function (`sum`)**:
   - Calculates the sum of the squares of digits of a number.

2. **Loop Detection Using a Set**:
   - Use a set to track numbers that have been seen before to detect cycles.
   - If `1` is reached, return `True` (indicating a happy number).
   - If a cycle is detected (the number repeats), return `False` (indicating it is not a happy number).

3. **Iterate Until Cycle or 1**:
   - Repeatedly apply the sum of squares operation to `n`.
   - If `1` is encountered, return `True`.
   - If the number repeats, return `False`.

---

## Code

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        
        def sum_of_squares(n):
            res = 0
            for i in str(n):
                res += int(i) ** 2
            return res
        
        r = n
        while r != 1:
            r = sum_of_squares(r)
            if r in s:
                return False
            s.add(r)
        return True
