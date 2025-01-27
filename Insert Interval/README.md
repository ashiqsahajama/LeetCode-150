# LeetCode 57: Insert Interval

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/insert-interval/)

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start, end]`, sorted by start time, and an interval `newInterval` representing an interval to insert.

Insert `newInterval` into `intervals` so that the resulting intervals are still sorted and non-overlapping. Return the new array of intervals.

### Constraints:
1. \( 0 \leq \text{intervals.length} \leq 10^4 \)
2. \( \text{intervals[i][0]} \leq \text{intervals[i][1]} \leq 10^5 \)
3. \( \text{newInterval.length} == 2 \)
4. \( 0 \leq \text{newInterval[0]} \leq \text{newInterval[1]} \leq 10^5 \)

### Examples:

| Input                                  | Output                      |
|----------------------------------------|-----------------------------|
| `intervals = [[1,3],[6,9]], newInterval = [2,5]` | `[[1,5],[6,9]]`              |
| `intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]` | `[[1,2],[3,10],[12,16]]` |
---

## Solution Explanation

This solution inserts the `newInterval` into the sorted list of intervals by following these steps:

1. **Initialize Result List**:
   - `res`: Stores merged intervals.

2. **Iterate Through Intervals**:
   - If the new interval ends before the current interval starts, append `newInterval` to the result and return all remaining intervals.
   - If the new interval starts after the current interval ends, append the current interval.
   - If there is overlap, merge the intervals by updating `newInterval` to the minimum start and maximum end.

3. **Add Remaining Intervals**:
   - Append the final `newInterval` after processing all intervals.

4. **Return Merged Intervals**:
   - Return the list of non-overlapping merged intervals.

---

## Code

```python
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:  # New interval comes before the current interval
                res.append(newInterval)
                return res + intervals[i:]  # Append remaining intervals
            elif newInterval[0] > intervals[i][1]:  # New interval comes after the current interval
                res.append(intervals[i])
            else:  # Overlapping intervals
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        
        res.append(newInterval)  # Add remaining new interval
        return res
