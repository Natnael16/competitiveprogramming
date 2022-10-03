class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bSearch(left, right,tar,leftBest=True):
            best = -1
            while left <= right:
                mid = (right + left)//2
                if nums[mid] > tar:
                    right = mid -1
                elif nums[mid] < tar:
                    left = mid + 1
                else:
                    best = mid
                    if leftBest:
                        right = mid - 1
                    else:
                        left = mid + 1
            return best
        return [bSearch(0,len(nums) - 1,target),bSearch(0,len(nums) - 1,target,False)]