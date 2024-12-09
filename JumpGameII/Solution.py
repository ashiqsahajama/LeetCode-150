class Solution:
    def jump(self, nums: List[int]) -> int:
        limit = 0
        max_reach = 0
        jump = 0
        for i in range(len(nums)-1):
            max_reach = max(max_reach,i+nums[i])
            if i==limit:
                jump+=1
                limit = max_reach
        return jump
