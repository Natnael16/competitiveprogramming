class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        if len(nums) < 2: return 0
        nums.sort()
        possible_max = nums[-1] - k
        
        possible_min =nums[0] + k
        
        res = nums[-1] - nums[0]
        # the minimum range is located between to concecutive elements of the array
        for num in range(len(nums) - 1):
            cur_max = max(possible_max , nums[num] + k)
            cur_min = min(possible_min , nums[num + 1] - k)
            res = min(res , cur_max - cur_min)
        return res