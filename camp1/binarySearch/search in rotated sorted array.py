class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        best = 0
        while left<= right:
            mid = left + (right - left)//2
            
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                best = mid
                right = mid - 1
        # print(best)
        if target == nums[best]:
            return best
        
        elif target > nums[best] and target <= nums[-1]:
            first = best + 1
            last = len(nums) - 1
        else:
            first = 0
            last = best - 1
        # print(first,last)
        while first <= last:
            middle = first + (last - first)//2
            
            if nums[middle] > target:
                last = middle - 1
            elif nums[middle] < target:
                first = middle + 1
            else:
                return middle
        return -1