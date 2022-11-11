class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        
        a, b , c = 0, 1, 2
        while c < len(nums):
            if nums[a] - nums[b] < nums[c] < nums[a] + nums[b] :
                return nums[a] + nums[b] + nums[c]
            a , b, c = a + 1, b + 1, c + 1
        return 0
            