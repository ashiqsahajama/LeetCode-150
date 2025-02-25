# LeetCode 295: Find Median from Data Stream

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/find-median-from-data-stream/)

Implement a data structure that efficiently supports:
1. `addNum(int num)`: Inserts a number into the data structure.
2. `findMedian()`: Returns the **median** of all elements in the structure.

### Constraints:
1. There will be at most \( 5 \times 10^4 \) calls to `addNum` and `findMedian`.
2. \( -10^5 \leq \text{num} \leq 10^5 \)
3. Calls to `findMedian` will always be valid.

---

## Solution Explanation

This solution uses **two heaps** to efficiently maintain the median in **logarithmic time**.

### Steps:

1. **Use Two Heaps**:
   - A **max-heap (`small`)** stores the **smaller half** of numbers (stored as negative values for heapq).
   - A **min-heap (`large`)** stores the **larger half** of numbers.

2. **Balance the Heaps**:
   - Ensure that `small` always contains the same number of elements or **one more** than `large`.

3. **Insert Numbers**:
   - Insert the new number into `small` first (as a negative value).
   - If necessary, move the smallest element from `small` to `large` to maintain order.
   - Balance the heaps if their sizes differ by more than one.

4. **Find the Median**:
   - If `small` has more elements, return its top.
   - If `large` has more elements, return its top.
   - If both heaps have equal size, return the average of their tops.

---

## Code

```python
import heapq

class MedianFinder:

    def __init__(self):
        # Max-Heap (negative values to simulate max behavior)
        self.small = []
        # Min-Heap
        self.large = []

    def addNum(self, num: int) -> None:
        # Add to max-heap (small)
        heapq.heappush(self.small, -num)

        # Maintain order by moving elements to the correct heap
        if (self.small and self.large and -self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))

        # Balance heaps to ensure size difference is at most 1
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        # If one heap is larger, return its top element
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]
        # If equal, return the average of the two top elements
        return (-self.small[0] + self.large[0]) / 2
