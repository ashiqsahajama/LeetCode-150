class Solution:
    def hIndex(self, citations: List[int]) -> int:
        r = sorted(citations,reverse=True)
        h=0

        for i in range(len(r)):
            if r[i]>=h+1:
                h+=1
        return h
