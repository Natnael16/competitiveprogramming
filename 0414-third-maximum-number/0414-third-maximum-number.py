class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        return nums[-3] if len(nums) > 2 else max(nums)