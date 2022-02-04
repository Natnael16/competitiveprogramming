class Solution(object):
    def removeDuplicates(self, nums):
        length = len(nums)
        i,j= 0,1   
        if length == 1 or length == 0:
            return
        maximum_val = max(nums) + 1
        while j != length:
            if nums[i] == nums[j]:
                nums[i]= maximum_val
            i += 1
            j += 1
        duplicates = length - nums.count(maximum_val)
        nums.sort()
        return duplicates