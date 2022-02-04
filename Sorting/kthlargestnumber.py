class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # for i in range(1,len(nums)):
        #     for j in range(i-1,-1,-1):      O(n^2)
        #         if int(nums[j+1]) > int(nums[j]) :
        #             temp = nums[j+1]
        #             nums[j+1] = nums[j]
        #             nums[j] = temp
        # return nums[k-1]
        nums = [int(i) for i in nums]
        nums.sort(reverse = True)     #O(nlog(n))
        return str(nums[k-1])