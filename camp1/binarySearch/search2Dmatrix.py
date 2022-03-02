class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) -1
        while left <= right:
            mid = left + (right - left)//2
            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][0] == target:
                return True
            else:
                left = mid + 1
        row = right
        left = 0
        right = len(matrix[row]) - 1
        while left <= right:
            mid2 = left + (right - left)//2
            if matrix[row][mid2] > target:
                right = mid2 - 1
            elif matrix[row][mid2] < target:
                left = mid2 + 1
            elif matrix[row][mid2] == target:
                return True
