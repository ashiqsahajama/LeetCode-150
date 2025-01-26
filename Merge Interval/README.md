
---

## Solution Explanation

This solution merges overlapping intervals by following these steps:

1. **Sort Intervals**:
   - Sort intervals based on the starting value to ensure processing in order.
   - Sorting allows merging adjacent intervals efficiently.

2. **Merge Intervals**:
   - Initialize an `output` list with the first interval.
   - Iterate through the remaining intervals:
     - If the current interval overlaps with the last interval in `output`, merge them by updating the end value.
     - If no overlap, append the interval to the `output` list.

3. **Return Result**:
   - Return the merged list of intervals.

---

## Code

```python
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])  # Sort intervals based on start times
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastk = output[-1][1]

            if lastk >= start:
                output[-1][1] = max(lastk, end)  # Merge overlapping intervals
            else:
                output.append([start, end])  # Add non-overlapping interval

        return output
