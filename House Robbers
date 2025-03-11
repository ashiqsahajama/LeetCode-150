#iterative memoisation 
class Solution:
    def rob(self, nums: List[int]) -> int:
        robery = [0]*(len(nums)+1)
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        robery[0]=0
        robery[1]=nums[0]
        for i in range(1,len(nums)):
            robery[i+1]=(max(robery[i],robery[i-1]+nums[i]))
        return robery[-1]
        
