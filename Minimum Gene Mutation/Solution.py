class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque()
        if endGene not in bank:
            return -1
        queue.append([startGene,0])
        visited = set()
        visited.add(startGene)
        genebank = set(bank)

        while queue:
            curr,step = queue.popleft()
            if curr == endGene:
                return step

            for c in 'ACGT':
                for i in range(len(curr)):
                    chk = curr[:i]+c+curr[i+1:]
                    if chk in genebank and chk not in visited:
                        queue.append([chk,step+1])
                        visited.add(chk)
        return -1
