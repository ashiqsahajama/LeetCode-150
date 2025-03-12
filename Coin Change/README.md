# LeetCode 322: Coin Change

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/coin-change/)

You are given an integer array `coins` representing different denominations and an integer `amount` representing a total sum of money. Return the **fewest number of coins** that you need to make up the given `amount`. If it's **not possible** to make that amount, return `-1`.

### Constraints:
1. `1 <= coins.length <= 12`
2. `1 <= coins[i] <= 2^31 - 1`
3. `0 <= amount <= 10^4`

### Examples:

| Coins         | Amount | Output | Explanation |
|--------------|--------|--------|-------------|
| `[1,2,5]`   | `11`   | `3`    | Use `5 + 5 + 1` to make `11` with `3` coins. |
| `[2]`       | `3`    | `-1`   | Not possible to make `3` using only `2`. |
| `[1]`       | `0`    | `0`    | No coins needed to make `0`. |

---

## Solution Explanation

This problem is solved using **Dynamic Programming**:

1. **Initialization**:
   - Create an array `dp` of size `amount + 1` initialized to `(amount + 1)`, which represents an unattainable value.
   - Set `dp[0] = 0` (0 coins are needed to make amount 0).

2. **Bottom-Up DP Approach**:
   - Iterate through `dp` from `0` to `amount`.
   - For each `coin` in `coins`, check if using this coin helps minimize the count:
     \[
     dp[i] = \min(dp[i], 1 + dp[i - coin])
     \]
   - This ensures that we always store the minimum number of coins required to make each amount.

3. **Final Output**:
   - If `dp[amount]` remains `(amount + 1)`, it means the amount is not possible to form, so return `-1`.
   - Otherwise, return `dp[amount]`.

---

## Code

```python
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            for j in coins:
                if i - j >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - j])
        if dp[-1] == (amount + 1):
            return -1
        return dp[-1]
