class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        for i in range(len(haystack)):
            if needle==haystack[i:i+m]:
                return i
        return -1

       
