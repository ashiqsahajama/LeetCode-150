class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        chk1 = {}
        chk2 = {}
        if len(s)!=len(pattern):
            return False
        
        for i in range(len(s)):
            a = s[i]
            b = pattern[i]
            if ((a in chk1 and chk1[a]!=b) or (b in chk2 and chk2[b]!=a)):
                 return False
            chk1[a] = b
            chk2[b] = a
        return True
        

        
