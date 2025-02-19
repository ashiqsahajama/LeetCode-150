class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        maxx = nums[0]

        for i in nums:
            curr = max(curr,0)
            curr+=i
            maxx = max(maxx,curr)
        return maxx
