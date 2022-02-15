class Solution:

    def maxFrequency(self, nums: List[int], k: int) -> int:
        i, j = 0, 1
        res = 1
        nums.sort()
        psum = nums[i]
        while j < len(nums):
            if i == j:
                j += 1
            elif ((j - i) * nums[j]) - psum <= k:
                psum += nums[j]
                if res < j - i + 1:
                    res = j - i + 1
                j += 1
            else:
                psum = psum - nums[i]
                i += 1
                if psum == 0:
                    psum = nums[i]
                # j = i + 1

        return res