class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i + 1] = 0
                nums[i] *= 2
        ans = []
        for num in nums:
            if num != 0:
                ans.append(num)
        return ans + ([0] *  (len(nums) - len(ans)))
            