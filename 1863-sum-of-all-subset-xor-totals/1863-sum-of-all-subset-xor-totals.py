class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans = 0
        def backtrack(ind, sum_):
            if ind > len(nums):
                return
            self.ans += sum_
            for i in range(ind+ 1 , len(nums)):
                backtrack(i,sum_ ^ nums[i])
        backtrack(-1,0)
        return self.ans