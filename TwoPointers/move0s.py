class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, j = 0,1
        if len(nums) == 1:
            return nums
        while j != len(nums):
            if nums[i] != 0:
                i+=1
                j+=1
            else:
                if nums[j] == 0:
                    j+=1
                elif nums[j] != 0:
                    t = nums[i]
                    nums[i] = nums[j]
                    nums[j] = t
                    i+=1
                    j+=1