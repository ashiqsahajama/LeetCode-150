class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        m = 0
        l = 0
        for i in range(len(s)):
            while (s[i] in res):
                    res.remove(s[l])
                    l+=1
            res.add(s[i])
            m = max(m,i-l+1)
        return m
        




        
