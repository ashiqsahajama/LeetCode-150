class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num)

        if (self.small and self.large and -self.small[0]>self.large[0]):
            heapq.heappush(self.large,-heapq.heappop(self.small))

        if len(self.small)>len(self.large)+1:
            heapq.heappush(self.large,-heapq.heappop(self.small))
        if len(self.large)>len(self.small)+1:
            heapq.heappush(self.small,-heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return -self.small[0]
        if len(self.small)<len(self.large):
            return self.large[0]
        return (-self.small[0]+self.large[0])/2
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
