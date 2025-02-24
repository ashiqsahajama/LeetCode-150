class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProf = []
        minCap = [(c,p) for c,p in zip(capital,profits)]
        heapq.heapify(minCap)
        for i in range(k):
            while minCap and minCap[0][0]<=w:
                c,p = heapq.heappop(minCap)
                heapq.heappush(maxProf,-1 * p)
            if not maxProf:
                break
            w += -1*heapq.heappop(maxProf)
        return w
        
