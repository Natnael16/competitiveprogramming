class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        number that is greater than the last element
        if mid > last num: record that and find to the right
            [3,4,1,2]
        '''
        n = len(nums)
        pivot  = n - 1
        
        left ,right = 0 , n - 1
        while left <= right:
            mid = left + (right - left )//2
            if nums[mid] < nums[pivot]:
                right = mid - 1
            else:
                pivot = mid
                left = mid + 1
        return nums[0] if pivot == n - 1 else nums[pivot + 1]
            