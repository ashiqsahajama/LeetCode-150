# LeetCode 373: Find K Pairs with Smallest Sums

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)

Given two **sorted** integer arrays `nums1` and `nums2` and an integer `k`, return the `k` pairs **(u, v)** with the smallest sums, where `u` is from `nums1` and `v` is from `nums2`.

### Constraints:
1. \( 1 \leq \text{nums1.length}, \text{nums2.length} \leq 10^5 \)
2. \( -10^9 \leq \text{nums1[i]}, \text{nums2[i]} \leq 10^9 \)
3. \( 1 \leq k \leq 10^4 \)

---

## Solution Explanation

This solution uses a **min-heap (priority queue)** to efficiently extract the smallest sum pairs.

### Steps:

1. **Use a Min-Heap to Store Pairs**:
   - Start by pushing the smallest possible sum pair `(nums1[0], nums2[0])` into the heap.
   - Track visited index pairs `(i, j)` using a `set`.

2. **Extract `k` Smallest Pairs**:
   - Pop the smallest sum pair from the heap.
   - Push the **next possible pairs** `(nums1[i+1], nums2[j])` and `(nums1[i], nums2[j+1])` if they haven't been visited.

3. **Maintain a Set of Visited Indices**:
   - Ensures that each pair is considered only once.

4. **Return the First `k` Pairs**:
   - Stop once `k` pairs are extracted.

---

## Code

```python
import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        heapq.heappush(heap, ([nums1[0] + nums2[0]], (0, 0)))
        visited = set((0, 0))
        res = []
        m, n = len(nums1), len(nums2)

        while k > 0 and heap:
            curr, (i, j) = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])

            if i + 1 < m and (i + 1, j) not in visited:
                heapq.heappush(heap, ([nums1[i + 1] + nums2[j]], (i + 1, j)))
                visited.add((i + 1, j))

            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(heap, ([nums1[i] + nums2[j + 1]], (i, j + 1)))
                visited.add((i, j + 1))

            k -= 1

        return res
