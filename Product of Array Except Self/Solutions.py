class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        suf = [1]*len(nums)

        l=len(nums)

        for i in range(1,l):
            pre.append(pre[i-1]*nums[i-1])
        
        for i in range(l-2,-1,-1):
            suf[i]=(suf[i+1]*nums[i+1])
        print(suf)
        print(pre)
        
        res  =[]

        for i in range(l):
            res.append(pre[i]*suf[i])
        return res
