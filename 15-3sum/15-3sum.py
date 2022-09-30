class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
#         # O(n^2logn) TLE
#         def bSearch(left, right, target):
#             while left <= right:
#                 mid = left + (right - left)//2
                
#                 if nums[mid] > target:
#                     right = mid - 1
#                 elif nums[mid] < target:
#                     left = mid + 1
#                 else:
#                     return nums[mid]
#             return -1
#         nums.sort()
#         ans = set()
        
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1,n):
#                 res = bSearch(j+1,n-1,-(nums[i] + nums[j]))
#                 if res != -1:
#                     ans.add((nums[i],nums[j],res))
#         return sorted(ans)
        ###########################################################
        nums.sort()
        [-4,-1,-1,0,1,2]
        n = len(nums)
        ans = set()
        for i in range(n):
            left ,right = i + 1, n-1
            while left < right:
                added = nums[left] + nums[right]
                if added > -(nums[i]):
                    right -=1
                elif added < -(nums[i]):
                    left += 1
                else:
                    ans.add((nums[i],nums[left],nums[right]))
                    right -= 1
                    
                    
        return sorted(ans)