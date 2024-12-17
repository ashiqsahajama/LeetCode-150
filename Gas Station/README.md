# LeetCode 150 Solutions

## Table of Contents
- [Gas Station](LeetCode/GasStation)

---

## Problem Explanations

### Gas Station

- **Problem:** [LeetCode Link](https://leetcode.com/problems/gas-station/)

  There are `n` gas stations along a circular route, where `gas[i]` is the amount of gas at station `i`, and `cost[i]` is the cost of gas required to travel to the next station.

  You start at one of the gas stations and must complete the circuit by visiting all stations exactly once and returning to the starting point. 

  Return the index of the starting gas station if you can complete the circuit, or `-1` if you cannot.

  **Constraints**:
  - The sum of `gas` must be greater than or equal to the sum of `cost` for a solution to exist.

---

### Solution Explanation

The solution uses a greedy approach to determine the valid starting gas station:

1. **Check Feasibility**:
   - If the total gas (`sum(gas)`) is less than the total cost (`sum(cost)`), it's impossible to complete the circuit, so return `-1`.

2. **Calculate Differences**:
   - Create an array `res` where each element is the difference between the gas at station `i` and the cost to travel to the next station: `res[i] = gas[i] - cost[i]`.
   - A positive difference means surplus gas, and a negative difference means a deficit.

3. **Iterate Through `res`**:
   - Track the cumulative sum (`tot`) as you iterate through the differences.
   - If `tot` becomes negative, reset it to `0` and set a flag `f = 0` to indicate a deficit.
   - If `tot` becomes positive again and `f` was previously `0`, update the potential starting point `r` to the current station index.

4. **Return the Result**:
   - After iterating through the entire array, the index `r` represents the starting gas station.

---
