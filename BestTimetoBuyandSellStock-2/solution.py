class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for i in range(len(prices)):
            if buy<prices[i]:
                profit += prices[i]-buy
                buy=prices[i]
            elif buy>prices[i]:
                buy = prices[i]
        return profit
            

      
