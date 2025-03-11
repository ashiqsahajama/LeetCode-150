class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n ==2:
            return 2
        prev = 2
        bef = 1
        for i in range(2,n):
            curr = prev + bef
            bef = prev
            prev = curr
        return curr

        
