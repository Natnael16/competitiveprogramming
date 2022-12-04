class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        # [2,5,3,9,5,3]
        # [2,7,10,19,24,27]
        # [27,25,20,17,8,3]
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        psum = 0
        for index, num in enumerate(nums):
            psum += num
            prefix[index] = psum
        psum = 0
        for index in range(n-1, -1, -1):
            psum += nums[index]
            suffix[index] = psum
        mini = [sum(nums)//n,n-1]
        for index in range(n - 1):
            left_av = prefix[index] // (index + 1)
            right_av = suffix[index + 1] // (n - index - 1)
            mini = min(mini , [abs(left_av - right_av),index])
        return mini[1]
            