class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j=len(s)-1
        while(j>0):
            if s[-1].isspace():
                s = s[:-1]
                j-=1
            else:
                break
        print(s)
        j=len(s)-1
        res = 0
        while(j>=0):
            if s[j].isalpha():
                res+=1
                j-=1
            else:
                break
        return res
            
       
