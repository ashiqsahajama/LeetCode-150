class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        has = Counter(magazine)

        for i in ransomNote:
            if i not in has or has[i]<=0:
                return False
            has[i]-=1
        return True
            
