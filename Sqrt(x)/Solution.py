class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x

        while l<=r:
            m = (l+r)//2
            if m*m == x:
                return m
            if m*m > x:
                r = m-1
            if m*m<x:
                l = m+1
        return r
        
