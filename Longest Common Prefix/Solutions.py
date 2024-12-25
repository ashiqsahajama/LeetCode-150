#Brute Force
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)<=1:
            return strs[0]
        a = strs[0]
        b = strs[1]
        x = 0

        if len(a)<len(b):
            x = len(a)
        else:
            x = len(b)
        
        c = ''
        for i in range(x):
            if a[i]==b[i]:
                c+=a[i]
            else:
                break
        if len(strs)==2:
            return c
        res = []
        for i in range(2,len(strs)):
            if strs[i]=="":
                return ""
            d = ""
            if len(strs[i])<len(c):
                x = len(strs[i])
            else:
                x = len(c)
            for j in range(x):
                print("word:",strs[i])
                if strs[i][j]==c[j]:
                    print("chk:",c[j])
                    d+=c[j]
                else:
                    break
            res.append(d)
        print(res)
        s = set(res)
        print(s)
        if len(s)==1:
            return res[0]
        elif len(s)>1:
            a = list(s)
            a = sorted(a,key=len)
            return a[0]
        else:
            return ""

            
        
        
