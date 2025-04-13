class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        queue.append([beginWord,0])
        visited = set()
        word = set()
        wordChk = set(wordList)
        for i in wordList:
            for j in i:
                word.add(j)
        while queue:
            curr,step = queue.popleft()
            if curr == endWord:
                return step+1
            for i in word:
                for j in range(len(curr)):
                    chk = curr[:j]+i+curr[j+1:]
                    if chk in wordChk and chk not in visited:
                        visited.add(chk)
                        queue.append([chk,step+1])
        return 0

        
