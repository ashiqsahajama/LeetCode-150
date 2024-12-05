class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = m-1
        b = n-1
        p = m+n-1

        while(b>=0):
            if nums1[a]>nums2[b] and a>=0:
                nums1[p]=nums1[a]
                a-=1
                p-=1
            else:
                nums1[p]=nums2[b]
                b-=1
                p-=1
            
