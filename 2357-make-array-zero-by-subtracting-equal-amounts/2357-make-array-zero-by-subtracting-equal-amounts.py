class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def getMin():
            mini = inf
            for num in nums:
                if num != 0:
                    mini = min(mini, num)
            return mini if mini != inf else 0
        total = sum(nums)
        count = 0
        while total:
            min_num = getMin()
            for ind, num in enumerate(nums):
                if num != 0:
                    total -= min_num
                    nums[ind] -= min_num
            count += 1
            
        return count