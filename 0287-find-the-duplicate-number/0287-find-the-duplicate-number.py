class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def counter(num):
            count = 0
            for i in nums:
                if i <= num: count += 1
            return count
        max_elem = max(nums)
        left , right = 1, max_elem
        while left <= right:
            mid = left + (right - left)//2
            count = counter(mid)
            if count > mid:
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        return best
                