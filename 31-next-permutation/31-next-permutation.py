class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """  
        # [0,1,3,6,5,4,2]
        
        n = len(nums)
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i + 1]:
                pivot_left = i
                back = n - 1
                while back > pivot_left and nums[back] <= nums[pivot_left]:
                    back -= 1
                nums[back],nums[pivot_left] = nums[pivot_left],nums[back]
                left , right = pivot_left + 1,n-1
                while left < right:
                    nums[left],nums[right] = nums[right],nums[left]
                    left += 1; right -= 1
                return 
        nums.reverse()