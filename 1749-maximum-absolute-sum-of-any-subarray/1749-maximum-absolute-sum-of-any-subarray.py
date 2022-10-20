class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        nums_len = len(nums)
        mini ,maxi = 0, 0 #max and min so far
        
        max_sum = -inf
        for back in range(nums_len - 1,-1,-1):
            min_so_far , max_so_far = mini,maxi
            mini= min(nums[back],nums[back] + min_so_far)
            maxi = max(nums[back],nums[back] + max_so_far)
            
            max_sum = max(abs(maxi), abs(mini),max_sum)
        return max_sum
        
            
            