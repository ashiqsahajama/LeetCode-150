class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r = defaultdict(list)

        for i in strs:
            r[tuple(sorted(i)].append(i)
        return (list(r.values()))
       
