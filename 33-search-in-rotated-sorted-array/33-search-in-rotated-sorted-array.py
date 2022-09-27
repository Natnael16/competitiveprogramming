class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pivot = n - 1
        
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left )//2
            if nums[pivot] > nums[mid]:
                right = mid -1
            else:
                pivot = mid
                left = mid + 1
                
        if pivot == n - 1:
            left, right = 0 , n -1
        elif target > nums[-1] :
            left , right = 0, pivot
        elif nums[-1] > target:
            left , right =  pivot + 1, n -1
        else:
            return n - 1
        
        # print(left, right)
        while left <= right:
            mid = left + (right - left )//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        return -1