class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        has = {}
        hat = {}

        for i in range(len(s)):
            a = s[i]
            b = t[i]
            if ((a in has and has[a] != b) or  
            (b in hat and hat[b] != a)):
                return False
            has[a] = b
            hat[b] = a
        return True
        
