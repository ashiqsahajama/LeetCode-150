# LeetCode 149: Max Points on a Line

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/max-points-on-a-line/)

Given an array of `points` representing coordinates \([x, y]\) on a 2D plane, return the **maximum number of points that lie on the same straight line**.

### Constraints:
1. \( 1 \leq \text{points.length} \leq 300 \)
2. \( -10^4 \leq x, y \leq 10^4 \)

---

## Solution Explanation

This solution **uses slopes to count collinear points**.

### Steps:

1. **Iterate Through Each Point (`i`) as a Reference**:
   - Create a dictionary `chk` to store the count of points with the same slope.
   - Initialize `res = 1` (at least one point exists).

2. **Compute the Slope for Each Pair (`i, j`)**:
   - If `b[0] == a[0]` (same x-coordinate), use `-inf` as slope (vertical line).
   - Otherwise, calculate the slope using **(y2 - y1) / (x2 - x1)**.
   - Store the slope in `chk` and update `res` with the maximum count.

3. **Return the Maximum Count of Points on a Line**.

---

## Code

```python
from collections import defaultdict
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 1
        for i in range(len(points)):
            chk = defaultdict(int)
            a = points[i]
            for j in range(i + 1, len(points)):
                b = points[j]
                if b[0] == a[0]:  # Vertical line case
                    slope = -float('inf')
                else:
                    slope = (b[1] - a[1]) / (b[0] - a[0])  # Compute slope
                chk[slope] += 1
                res = max(res, chk[slope] + 1)
        return res
