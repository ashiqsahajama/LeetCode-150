class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        def sum(n):
            res = 0
            for i in str(n):
                res+=int(i)**2
            return res
        r = n
        while(r!=1):
            r = sum(r)
            if r in s:
                return False
            s.add(r)
        return True
        
