class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r = {}

        for i in range(len(nums)):
            if r.get(target-nums[i])!=None:
                return (i,r[target-nums[i]])
            else:
                r[nums[i]] = i
