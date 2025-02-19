# LeetCode 918: Maximum Sum Circular Subarray

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/maximum-sum-circular-subarray/)

Given a **circular integer array** `nums`, return the **maximum possible sum of a non-empty subarray**. The subarray can be **non-contiguous** due to the circular nature of the array.

### Constraints:
1. \( 1 \leq \text{nums.length} \leq 3 \times 10^4 \)
2. \( -3 \times 10^4 \leq \text{nums[i]} \leq 3 \times 10^4 \)

---

## Solution Explanation

This solution extends **Kadane’s Algorithm** to handle circular subarrays efficiently.

### Steps:

1. **Find the Maximum Subarray Sum (Kadane’s Algorithm)**:
   - This gives the **maximum subarray sum** for a **non-circular** case.

2. **Find the Minimum Subarray Sum**:
   - This helps in calculating the **maximum circular sum** using `total - minSubarraySum`.

3. **Handle Edge Case**:
   - If all elements are negative, the circular max sum formula `total - minSubarraySum` leads to `0`, which is incorrect.
   - In this case, return `maxSubarraySum`.

4. **Return the Maximum of Both Cases**:
   - The result is `max(maxSubarraySum, total - minSubarraySum)`.

---

## Code

```python
from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr = 0
        currmn = 0
        mx = nums[0]
        mn = nums[0]
        tot = 0

        for i in nums:
            # Kadane's Algorithm for max subarray sum
            curr = max(curr, 0) + i
            mx = max(mx, curr)

            # Kadane's Algorithm for min subarray sum
            currmn = min(currmn, 0) + i
            mn = min(mn, currmn)

            # Total sum of the array
            tot += i

        # If the entire array is taken as min sum, return normal max subarray sum
        if tot == mn:
            return mx

        # Return max of non-circular and circular subarray sum
        return max(mx, tot - mn)
