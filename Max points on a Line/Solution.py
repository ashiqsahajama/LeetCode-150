class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 1
        for i in range(len(points)):
            chk = defaultdict(int)
            a = points[i]
            for j in range(i+1,len(points)):
                b = points[j]
                if b[0]==a[0]:
                    slope = -float('inf')
                else:
                    slope = (b[1]-a[1])/(b[0]-a[0])
                chk[slope]+=1
                res = max(res,chk[slope]+1)
        return res

        
