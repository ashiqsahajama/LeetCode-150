class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d =set()
        i = 0

        for j in range(len(nums)):
            print(nums[j])
            if j-i>k and len(d)>0:
                d.remove(nums[i])
                i+=1
            if nums[j] in d:
                return True
            d.add(nums[j])
        return False


    
