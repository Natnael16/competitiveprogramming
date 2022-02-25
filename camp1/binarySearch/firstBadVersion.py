class Solution:

    def leftOrRight(self, nums):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(nums[mid]):
                best = mid
                right = mid - 1
            elif not isBadVersion(nums[mid]):
                left = mid + 1
        return nums[best]

    def firstBadVersion(self, n: int) -> int:
        # nums = list(range(1,n+1))
        return self.leftOrRight(range(1, n + 1))
