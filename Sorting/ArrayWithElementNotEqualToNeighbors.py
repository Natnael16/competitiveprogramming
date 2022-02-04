class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        while True:
            count = 0
            for i in range(1,len(nums)-1):
                if (nums[i-1] + nums [i+1]) / 2 == nums[i]:
                    temp = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = temp
                    count += 1
            if count == 0:
                break
        return nums