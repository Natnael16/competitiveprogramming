class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        largest = []
        for i in range(int(len(nums)/2)):
            largest.append(nums[0]+nums[-1])
            nums.pop()
            nums.pop(0)                       ###best memory usage 
        return max(largest)