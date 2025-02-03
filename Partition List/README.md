# LeetCode 15: 3Sum

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/3sum/)

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that:
1. \( i \neq j \neq k \),
2. \( nums[i] + nums[j] + nums[k] = 0 \),
3. The solution set must not contain duplicate triplets.

### Constraints:
1. `0 <= nums.length <= 3000`
2. `-10^5 <= nums[i] <= 10^5`

### Examples:

| Input                        | Output                                  |
|------------------------------|-----------------------------------------|
| `nums = [-1, 0, 1, 2, -1, -4]` | `[[-1, -1, 2], [-1, 0, 1]]`             |
| `nums = []`                  | `[]`                                    |
| `nums = [0]`                 | `[]`                                    |

---

## Solution Explanation

This solution efficiently finds all unique triplets that sum to zero using a sorted array and a two-pointer approach:

1. **Sorting**:
   - Sort the array to enable efficient two-pointer traversal and easy duplicate handling.

2. **Iterate Through Array**:
   - Use a loop to fix one element of the triplet (`nums[i]`) at a time.
   - Skip duplicate values for `nums[i]` to ensure unique triplets.

3. **Two-Pointer Technique**:
   - Use two pointers (`j` and `k`) to find the other two elements:
     - `j` starts right after `i`.
     - `k` starts at the end of the array.
   - Check the sum:
     - If the sum is greater than 0, decrement `k` to reduce the sum.
     - If the sum is less than 0, increment `j` to increase the sum.
     - If the sum is 0, add the triplet `[nums[i], nums[j], nums[k]]` to the result and move `j` forward while skipping duplicates.

4. **Break Condition**:
   - Break the loop early if `nums[i] > 0`, as no triplet can sum to zero if the first element is positive.

5. **Return Result**:
   - Return the list of unique triplets.

---

## Code

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array first
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicates for left and right pointers
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return result
