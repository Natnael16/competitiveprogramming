class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = -1
        nums_len = len(nums)
        for num in nums:
            if nums[abs(num)-1] < 0:
                duplicate = abs(num)
            else:
                nums[abs(num)-1] *= -1
        for missing in range(1, nums_len + 1):
            if nums[missing - 1] > 0:
                return [duplicate, missing]
                
                
        
        