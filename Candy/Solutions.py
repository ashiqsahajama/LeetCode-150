class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        res_l = [1]*l
        res_r = [1]*l
        res = [1]*l
        for i in range(1,l):
            if ratings[i]>ratings[i-1]:
                res_l[i]=res_l[i-1]+1
        for i in range(l-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                res_r[i]=res_r[i+1]+1
        for i in range(l):
            res[i]=max(res_l[i],res_r[i])
        return sum(res)
