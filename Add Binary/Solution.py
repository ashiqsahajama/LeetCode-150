class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = []
        i,j = len(a)-1,len(b)-1
        while i>=0 or j>=0 or carry:
            c = int(a[i]) if i>=0 else 0
            d = int(b[j]) if j>=0 else 0

            total = c + d + carry
            res.append(str(total%2))
            carry = total//2
            i-=1
            j-=1
        return "".join(res[::-1])



