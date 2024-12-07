class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0]==0 and len(nums)>=2:
            return False
        elif nums[0]!=0 and len(nums)==2:
            return True
        elif len(nums)==1:
            return True
        f = nums[0]
        for i in range(1,len(nums)-1):
            print(f)
            f = max(f,i+nums[i])
            print(f)
            if f>=len(nums)-1:
                return True
            elif f==i+nums[i] and f!=len(nums)-1 and nums[i]==0:
                return False
        print(f)
        return False
        
