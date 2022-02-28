import math


class Solution:

    def dividor(self, arr, num):
        total = 0
        for i in arr:
            total += (int(math.ceil(i / num)))
        return total

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 0
        right = len(nums) - 1
        # best = -1
        while left <= right:
            mid = left + (right - left) // 2

            fun = self.dividor(nums, nums[mid])
            print(fun)
            if fun <= threshold:
                best = fun
                right = mid - 1
            else:
                left = mid + 1
        return best