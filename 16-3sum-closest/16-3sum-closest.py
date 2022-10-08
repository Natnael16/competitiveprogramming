class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
         # [-4,-1,2,2,5]  1   -1 result - target 4,7,4
         #         | |
         #5 > 2
            
        def closestSum(left, right, tar):
            c_sum = inf 
            while left < right:
                tot = nums[right] + nums[left]

                if abs(tot - tar) < abs(c_sum - tar): c_sum = tot
                if tot == tar: return tot
                elif tot > tar: right -= 1
                else: left += 1
            return c_sum
  
        n = len(nums)
        nums.sort()
        close_sum = inf
        for fixed in range(n):
            twoSum = closestSum(fixed + 1, n -1,target - nums[fixed])
            if abs(target - (nums[fixed] + twoSum)) < abs(target - close_sum):
                close_sum = nums[fixed] + twoSum
            
        return close_sum
        
        