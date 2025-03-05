class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        a = x
        b = 0

        while a>0:
            c = a%10
            b = b*10+c
            a //=10
        return b==x
        
