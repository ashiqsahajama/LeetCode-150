class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            #buy = min(buy,prices[i])
            if prices[i]<buy:
                buy = prices[i]
            elif prices[i]-buy>profit:
                profit = prices[i]-buy
        return profit

