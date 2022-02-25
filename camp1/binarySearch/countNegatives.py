class Solution:

    def isLess(self, num):
        if num < 0:
            return True

    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0

        for i in grid:
            left = 0
            right = len(i) - 1
            best = len(i)
            while left <= right:
                mid = left + (right - left) // 2
                if self.isLess(i[mid]):
                    best = mid
                    right = mid - 1
                else:
                    left = mid + 1
            leng = len(i) - best
            total += leng
        return total