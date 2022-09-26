class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     tot = prod(nums)
    #     ans = []
    #     for i in nums:
    #         ans.append(tot i)
    #     return ans
    # [1, 2 ,6, 24]
    # [24,24,12,4]
        forward = []
        backward = deque([])
        tot= 1
        n = len(nums)
        for num in nums:
            tot = tot * num
            forward.append(tot)
        tot = 1
        for i in range(n-1,-1,-1):
            tot *= nums[i]
            backward.appendleft(tot)
        ans = []
        for ind in range(n):
            left , right = ind - 1, ind + 1
            if left >= 0 and right < n:
                ans.append(backward[right] * forward[left])
            elif left >= 0:
                ans.append(forward[left])
            elif right < n:
                ans.append(backward[right])
        return ans
    