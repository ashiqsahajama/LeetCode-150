class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        countT = {}
        for i in t:
            countT[i] = countT.get(i,0)+1
        window = {}

        have,need = 0,len(countT)
        res = [-1,-1]
        minl = float('inf')
        l ,r =0,0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0)+1

            if c in countT and countT[c]==window[c]:
                have+=1
            
            while have==need:
                if(r-l+1)<minl:
                    res = [l,r]
                    minl = r-l+1
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if minl!=float('inf') else "" 

