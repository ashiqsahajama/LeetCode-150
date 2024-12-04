# LeetCode 150 Solutions

## Table of Contents
- [Best Time to Buy and Sell Stock](LeetCode/BestTimeToBuyAndSellStock)

## Problem Explanations

### Best Time to Buy and Sell Stock

- **Problem:** [LeetCode Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

  You are given an array where `prices[i]` is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

- **Solution Explanation:**
  - This problem can be solved efficiently using #use kadanes algorithm approach, to update buy if current element is less than buy and update profit if buy-current val is greater than old profit.
