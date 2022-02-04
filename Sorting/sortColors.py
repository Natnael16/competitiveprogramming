class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums)-1):
            small = nums[i]
            index = i
            for j in range(i+1,len(nums)):
                if small > nums[j]:
                    small = nums[j]
                    index = j
            nums[index] = nums[i] 
            nums[i] = small