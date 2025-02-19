class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr = 0
        currmn = 0
        mx = nums[0]
        mn = nums[0]
        tot = 0
        for i in nums:
            curr = max(curr,0)
            curr+=i
            mx = max(mx,curr)

            currmn = min(currmn,0)
            currmn += i
            mn = min(mn,currmn)

            tot += i
        if tot == mn:
            return mx
        return max(mx, tot-mn)
        
