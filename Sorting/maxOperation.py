class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == k and (nums[i] != -1 and nums[j] != -1 ):
                    nums[i] = -1
                    nums[j] = -1 ### timelimit error
                    count += 1
        return count