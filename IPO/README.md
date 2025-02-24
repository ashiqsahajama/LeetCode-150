# LeetCode 502: IPO (Initial Public Offering)

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/ipo/)

You are given `k` projects, an initial capital `w`, and two lists:
- `profits[i]`: The profit from project `i`.
- `capital[i]`: The minimum capital required to start project `i`.

Your goal is to maximize your capital by selecting at most `k` projects. At each step, you can only start a project if you have at least the required capital.

### Constraints:
1. \( 1 \leq k \leq 10^5 \)
2. \( 0 \leq w \leq 10^9 \)
3. \( n == \text{profits.length} == \text{capital.length} \)
4. \( 0 \leq \text{profits[i]}, \text{capital[i]} \leq 10^9 \)

---

## Solution Explanation

This solution uses a **greedy approach with two heaps** to efficiently select the most profitable projects.

### Steps:

1. **Min-Heap for Available Projects**:
   - Store projects as `(capital, profit)`, sorted by capital.
   - This allows extracting the **cheapest** projects that can be started with the current capital.

2. **Max-Heap for Profitable Projects**:
   - Once a project is available, push its profit (negative value) into a **max-heap**.
   - Extract the **most profitable** project from this heap to maximize capital.

3. **Execute Up to `k` Projects**:
   - In each iteration, pop the **most profitable** project and add its profit to `w`.
   - Stop early if no projects are available.

4. **Return Final Capital**:
   - The maximum possible capital after completing at most `k` projects.

---

## Code

```python
import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProf = []
        minCap = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minCap)  # Min-Heap: Sort projects by capital required

        for _ in range(k):
            # Move projects we can afford into the max heap
            while minCap and minCap[0][0] <= w:
                c, p = heapq.heappop(minCap)
                heapq.heappush(maxProf, -p)  # Max-Heap: Store profits as negative values
            
            if not maxProf:  # If no profitable projects left, stop early
                break

            # Pick the most profitable available project
            w += -heapq.heappop(maxProf)

        return w
