class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        hash = {
            ')':'(',
            ']':'[',
            "}":"{"
        }
        stack = []
        for i in s:
            if i in hash.values():
                stack.append(i)
            elif len(stack)>=1 and stack[-1]==hash[i]:
                stack.pop()
            else:
                return False
        return not stack
