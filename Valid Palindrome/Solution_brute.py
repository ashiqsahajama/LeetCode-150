class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = ""
        for i in s:
            if i.isalnum()==True:
                b+=i.lower()
        return b[::-1]==b
