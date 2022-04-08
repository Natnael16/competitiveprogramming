class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        slow = 0
        res = 0
        min_num , max_num  = sys.maxsize, -sys.maxsize
        while slow < len(nums) - 1:
            fast = slow + 1
            while fast < len(nums):
                min_num = min(nums[fast],nums[slow],min_num)
                max_num = max(nums[fast],nums[slow],max_num)
                res += (max_num - min_num)
                fast += 1
            min_num , max_num  = sys.maxsize, -sys.maxsize
            slow += 1
        return res
