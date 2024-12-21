class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        max_l = height[i]
        max_r = height[j]
        res = 0

        while(i<j):
            if height[i]<=height[j]:
                max_l=max(max_l,height[i])
                res+=max_l-height[i]
                i+=1
            else:
                max_r = max(max_r,height[j])
                res+=max_r-height[j]
                j-=1
        return res
        
