class Solution:
    def counter(self,num,arr):
        count = 0
        for n in arr:
            if n <= num:
                count += 1
        return count
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = max(nums)
        while left < right:
            mid = left + (right - left)//2
            if self.counter(mid,nums) > mid:
                right = mid
            else:
                
                left = mid + 1
        # print(left,right,mid)
        return left
