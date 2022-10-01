class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        see_left = [1] * n
        see_right= [1] * n
        
        for ind in range(1, n):
            if nums[ind] <= nums[ind - 1]:
                see_left[ind] += see_left[ind - 1]
        for ind in range(n - 2,-1,-1):
            if nums[ind] <= nums[ind + 1]:
                see_right[ind] += see_right[ind + 1]
        ans = []
        # print(see_left, see_right)
        for i in range(1, n -1 ):
            if see_left[i - 1] >= k and see_right[i + 1] >= k:
                ans.append(i)

        return ans