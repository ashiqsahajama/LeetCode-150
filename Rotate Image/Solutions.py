class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        top = 0
        bottom = n
        left = 0
        right = n

        while(top<bottom and left<right):
            for i in range(left,right):
                a = matrix[top][i]
                matrix[top][i] = matrix[i][top]
                matrix[i][top] = a
            top +=1
            left +=1
        print(matrix)
        for i in range(n):
            matrix[i] = matrix[i][::-1]
