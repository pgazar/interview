# Search 2D Matrix
# You are given an m x n 2-D integer array matrix and an integer target.

# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.

# Can you write a solution that runs in O(log(m * n)) time?

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        rows,cols = len(matrix) ,len(matrix[0]) # matrix[[1,2] , [3,4]]
        toprow = 0
        botrow = rows - 1

        while toprow <= botrow:
            midrow = (toprow + botrow)//2

            if target > matrix[midrow][-1]: # last value of the row
                toprow = midrow + 1

            elif target < matrix[midrow][0]:
                botrow = midrow - 1

            else:
                break
       
        if not (toprow <= botrow):
            return False
        midrow = (toprow + botrow) // 2

        l=0
        r=cols-1

        while l <= r:
            mid = (l+r)//2
            if target < matrix[midrow][mid]:
                r = mid-1
            elif target > matrix[midrow][mid]:
                l = mid+1
            else:
                return True
            
        return False