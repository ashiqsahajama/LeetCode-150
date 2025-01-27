# LeetCode 452: Minimum Number of Arrows to Burst Balloons

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

You are given an array of `points` where `points[i] = [start, end]` represents the horizontal position of a balloon. An arrow shot at `x` will burst a balloon if `start ≤ x ≤ end`.

Return the **minimum number of arrows** that must be shot to burst all balloons.

### Constraints:
1. \( 1 \leq \text{points.length} \leq 10^5 \)
2. \( \text{points[i][0]} \leq \text{points[i][1]} \leq 2^{31} - 1 \)

### Examples:

| Input                          | Output |
|--------------------------------|--------|
| `points = [[10,16],[2,8],[1,6],[7,12]]` | `2`    |
| `points = [[1,2],[3,4],[5,6],[7,8]]`    | `4`    |
| `points = [[1,2],[2,3],[3,4],[4,5]]`    | `2`    |

**Explanation for Example 1**:

- We can burst the balloons using two arrows:
  - One arrow at `x = 6` to burst `[1,6]` and `[2,8]`.
  - Another arrow at `x = 12` to burst `[7,12]` and `[10,16]`.

---

## Solution Explanation

This solution finds the minimum number of arrows using a **greedy approach**:

### Steps:

1. **Sort the Balloons by End Position**:
   - Sorting the intervals based on their ending position ensures the earliest possible burst.
   
2. **Iterate Through Sorted Balloons**:
   - Use a variable `crr` to track the last position where an arrow was shot.
   - If the start of the current balloon is greater than `crr`, it means a new arrow is needed.
   - Update `crr` to the current balloon's end and increment the arrow count.

3. **Return the Number of Arrows**:
   - The result gives the minimum number of arrows needed to burst all balloons.

---

## Code

```python
from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda i: i[1])  # Sort by end of intervals
        crr = float('-inf')
        res = 0

        for s, e in points:
            if s > crr:  # If balloon starts after last arrow shot
                res += 1
                crr = e  # Shoot arrow at end of current balloon
        
        return res
