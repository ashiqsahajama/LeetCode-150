#o(n) space

class Solution:
    def trap(self, height: List[int]) -> int:
        max_l =[height[0]]
        max_r = [1]*len(height)
        max_r[-1]=0
        m = 0
        n = 0
        z = 0

        for i in range(1,len(height)):
            m = max(m,height[i-1])
            max_l.append(m)
        
        for i in range(len(height)-2,-1,-1):
            n = max(n,height[i+1])
            max_r[i]=n
        print(max_r)
        print(max_l)
        for i in range(len(height)):
            k = min(max_l[i],max_r[i])-height[i]
            if k>0:
                z+=k
        return z

        
