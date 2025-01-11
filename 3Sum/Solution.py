class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        i = 0
        res = []
        for i in range(len(nums)-1):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            if (nums[i]>0):
                break 
            j = i+1
            k = len(nums)-1

            while(j<k):
                s = nums[i]+nums[j]+nums[k]
                if(s>0):
                    k-=1
                elif(s<0):
                    j+=1
                elif (s==0):
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while(nums[j]==nums[j-1] and j<k):
                        j+=1
        return res
        
