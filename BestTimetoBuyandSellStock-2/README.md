# LeetCode 150 Solutions

## Table of Contents
- [Best Time to Buy and Sell Stock II](LeetCode/BestTimeToBuyAndSellStockII)

---

## Problem Explanations

### Best Time to Buy and Sell Stock II

- **Problem:** [LeetCode Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

  You are given an integer array `prices` where `prices[i]` is the price of a given stock on the ith day. You may decide to buy and/or sell the stock on each day. You can buy and sell the stock multiple times, but you must buy before you sell.

  Find and return the maximum profit you can achieve.

- **Solution Explanation:**
  - In this problem, you can make multiple transactions (buying and selling on different days) to maximize the total profit.
  - The algorithm tracks the `buy` price, and each time a price is higher than the `buy` price, it calculates the profit and updates `buy` to the current price for the next possible transaction.
  - The total profit is accumulated by adding the difference between selling price and buying price when prices increase.
 
  - The difference between first and second is , in second we are allowed to buy and sell multiple times.So when we encounter a profit then be buy the next day and it buy is more then we buy another day.

---
