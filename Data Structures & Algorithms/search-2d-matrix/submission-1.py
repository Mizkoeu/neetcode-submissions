class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search
        l, r = 0, len(matrix)-1
        row = 0
        while l<=r:
            m = (l+r)//2
            if matrix[m][0] <= target and target <= matrix[m][-1]:
                row = m
                break
            if matrix[m][0] > target:
                r = m-1
            else:
                l = m+1
        l, r, = 0, len(matrix[0])-1
        print(row, l, r)
        while l<=r:
            m = (l+r)//2
            if matrix[row][m] == target:
                return True
            if matrix[row][m] > target:
                r = m-1
            else:
                l = m+1
        return False