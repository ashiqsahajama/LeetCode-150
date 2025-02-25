class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        l = 0
        r = (r*c)-1

        while l<=r:
            mid = (l+r)//2
            mid_r = mid//c
            mid_c = mid%c

            if matrix[mid_r][mid_c]==target:
                return True
            elif matrix[mid_r][mid_c]<target:
                l = mid+1
            elif matrix[mid_r][mid_c]>target:
                r = mid-1
        return False
