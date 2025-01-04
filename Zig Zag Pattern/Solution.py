class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        res = ""
        for r in range(numRows):
            ne = (numRows-1)*2
            for i in range(r,len(s),ne):
                res+=s[i]
                if(r>0 and r<numRows-1 and i+ne-(2*r)<len(s)):
                    res+=s[i+ne-(2*r)]
        return res
        
