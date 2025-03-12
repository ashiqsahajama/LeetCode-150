class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount ==0:
            return 0
        dp = [(amount+1)]*(amount+1)
        dp[0] = 0
        for i in range(len(dp)):
            for j in coins:
                if i-j>=0:
                    dp[i]=min(dp[i],1+dp[i-j])
        print(dp)
        if dp[-1]==(amount+1):
            return -1
        return dp[-1]
                
        
        
