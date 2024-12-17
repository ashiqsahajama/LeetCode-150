class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        res= []
        for i in range(len(gas)):
            res.append(gas[i]-cost[i])
        print(res)
        tot = 0
        r = 0
        t = 0
        f = 1

        for i in range(len(res)):
            tot+=res[i]
            if tot<0:
                tot = 0
                f = 0
            elif f == 0 and tot>=0:
                r = i
                f = 1
        return r
            
