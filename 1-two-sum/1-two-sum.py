class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = []
        for ind , num in enumerate(nums):
            sorted_nums.append((num , ind))
        sorted_nums.sort()
        
        i , j = 0 , len(nums) - 1
        
        while i <= j:
            tot = sorted_nums[i][0] + sorted_nums[j][0]
            
            if tot == target: return [sorted_nums[i][1], sorted_nums[j][1]]
            elif tot > target: j -= 1
            else: i += 1