class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left , right = 0,0
        result = 0
        count_1 , count_0 = 0, 0
        if len(nums) == 1:
            if nums[0] == 1:
                return 1
        while right < len(nums) and left < len(nums):
            
            if nums[right] == 0:
                count_0 += 1
            else:
                count_1 += 1
            if count_0 < k:
                if right - left + 1 > result:
                    result = right - left + 1
                right += 1
            elif count_0 > k:
                if nums[left] == 0:
                    count_0 -= 1
                else:
                    count_1 -= 1
                left += 1
                if nums[right] == 0:
                    count_0 -= 1
                else:
                    count_1 -= 1
            elif count_0 == k:
                if right - left + 1 > result:
                    result = right - left + 1
                right += 1
        return result
                