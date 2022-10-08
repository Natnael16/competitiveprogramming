# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         def bSearch(arr , tar , hi ,lo):
#             while lo <= hi:
#                 mid = (hi + lo)//2
                
#                 if arr[mid] > tar:
#                     hi = mid - 1
#                 elif arr[mid] < tar:
#                     lo = mid + 1
#                 else:
#                     return mid
#             return -1
#         for row in matrix:
#             found = bSearch(row,target,len(row)-1,0)
#             if found != -1:
#                 return True
#         return False
# if less than cur go left elif greater go down

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        row, col = 0,m - 1
        while 0 <= row < n and 0 <= col < m:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else: return True
        return False