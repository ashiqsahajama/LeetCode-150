class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n==0:
                return 1
            if x==0:
                return 0
            if n%2==0:
                res = helper(x,n//2)
                return res*res
            return x*helper(x,n-1)
        a = helper(x,abs(n))
        if n<0:
            return 1/a
        return a

        
    
        
