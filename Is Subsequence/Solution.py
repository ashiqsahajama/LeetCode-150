class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = s+"*"+t
        b = ""
        i = 0
        j = len(s)+1

        while(i<j and j<len(a)):
            if a[i] == a[j]:
                b+=a[i]
                i+=1
                j+=1
            else:
                j+=1
        return s==b


        
