class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda i:i[1])
        crr = float('-inf')
        res = 0
        for s,e in points:
            if s > crr:
                res+=1
                crr = e
        return res
            

        
