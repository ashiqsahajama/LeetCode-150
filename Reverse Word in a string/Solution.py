class Solution:
    def reverseWords(self, s: str) -> str:
        s = s+"*"
        print(s)
        res = []
        i = 0
        d = ""
        r = []

        while(i<len(s)):
            if s[i].isalnum()==True:
                print(s[i])
                d += s[i]
                i+=1
            else:
                res.append(d)
                d = ""
                i+=1
        for i in range(len(res)-1,-1,-1):
            if res[i].isalnum()==True:
                r.append(res[i])
        return " ".join(r)
        
