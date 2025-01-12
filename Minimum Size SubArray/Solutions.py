class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        m = float(inf)
        total = 0
        for j in range(len(nums)):
            total+=nums[j]
            while total>=target:
                m = min(m,j-i+1)
                total -=nums[i]
                i+=1
        return 0 if m==float(inf) else m

    
