class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def recur(nums):
            if len(nums) == 1:
                return nums[0]
            else:
                return max(nums[0]-recur(nums[1:]),nums[-1]-recur(nums[:-1]))
        if recur(nums)>=0: 
            return True
        else: False