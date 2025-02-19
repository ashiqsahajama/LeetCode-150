class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        m = []
        for i in nums:
            heapq.heappush(m,-i)
        while k>0:
            a = heapq.heappop(m)
            k-=1
        return -a
        
