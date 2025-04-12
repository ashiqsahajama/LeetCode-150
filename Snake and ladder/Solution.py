class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()
        def getpos(pos):
            r = (pos-1)//length
            c = (pos-1)%length
            if r%2:
                c = length-c-1
            return [r,c]
        queue = deque()
        visited = set()
        queue.append([1,0])
        visited.add(1)
        while queue:
            curr,moves = queue.popleft()

            for val in range(1,7):
                nextstep = curr + val
                r,c = getpos(nextstep)
                if board[r][c]!= -1:
                    nextstep = board[r][c]
                if nextstep == length*length:
                    return moves+1
                if nextstep not in visited:
                    visited.add(nextstep)
                    queue.append([nextstep,moves+1])
        return -1


        
