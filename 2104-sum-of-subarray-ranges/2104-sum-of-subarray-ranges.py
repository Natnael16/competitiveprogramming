class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            minn = nums[i]
            maxx = nums[i]
            for j in range(i, len(nums)):
                if nums[j] > maxx:
                    maxx = nums[j]
                if nums[j] < minn:
                    minn = nums[j] 
                answer += (maxx - minn)
        return answer