#optimal than sorting , take the count array which has the character count for each item in the input.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r = defaultdict(list)

        for i in strs:
            count = [0]*26
            for j in i:
                count[ord(j)-ord('a')]+=1
            r[tuple(count)].append(i)
        return (list(r.values()))
       
