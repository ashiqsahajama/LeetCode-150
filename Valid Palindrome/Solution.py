class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        ans = True
        if not s:
            return True

        while(i<=j):
            if s[i].lower()==s[j].lower():
                i+=1
                j-=1
            elif s[i].isalnum()== False:
                i+=1
            elif s[j].isalnum()== False:
                j-=1
            else:
                return False
        return ans
