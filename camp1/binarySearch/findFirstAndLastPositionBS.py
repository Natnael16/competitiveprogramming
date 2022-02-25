class Solution:
    def leftOrRight(self,nums,target,isFirst):
        left = 0 
        right = len(nums) - 1 
        best = -1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                if isFirst:
                    best = mid
                    right = mid -1
                else:
                    best = mid
                    left = left + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return best
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.leftOrRight(nums,target,True)
        right = self.leftOrRight(nums,target,False)
        return[left,right]
