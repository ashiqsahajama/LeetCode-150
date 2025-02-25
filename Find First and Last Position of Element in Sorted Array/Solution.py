class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarysearch(nums,target,left):
            l = 0
            r = len(nums)-1
            i = -1
            while l<=r:
                mid = (l+r)//2
                if nums[mid]<target:
                    l = mid + 1
                elif nums[mid]>target:
                    r = mid - 1
                else:
                    if left:
                        i = mid
                        r = mid -1
                    else:
                        i = mid
                        l = mid +1
            return i
        a = binarysearch(nums,target,True)
        b = binarysearch(nums,target,False)
        return [a,b]




