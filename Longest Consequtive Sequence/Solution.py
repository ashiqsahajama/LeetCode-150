class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        has = set(nums)
        mx = 0

        for i in nums:
            m = 1
            if i-1 in has:
                continue
            while(i+1 in has):
                m+=1
                i+=1
            mx = max(m,mx)
        return mx


        
