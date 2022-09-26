class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = nums[-1]
        
        for i in range(n-2,-1,-1):
            nums[i] = max(nums[i], nums[i] + nums[i + 1])
            max_sum = max(max_sum , nums[i])
        return max_sum