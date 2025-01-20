#o(m+n) space solution , can reduce the space in the next solution.
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        hasr = set()
        hasc = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] ==0:
                    hasr.add(i)
                    hasc.add(j)
        
        for i in hasr:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        
        for i in range(len(matrix)):
            for j in hasc:
                matrix[i][j] = 0

        
