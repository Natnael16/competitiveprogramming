class Solution:
    def maxProduct(self, nums: List[int]) -> int:
       
        ans = max(nums)
        maxi , mini = nums[-1] , nums[-1]
        # set max and min from self and num * maxi and num  * mini
        
        for i in range(len(nums) - 2, -1,-1):
            temp = maxi
            maxi = max(nums[i], nums[i]* maxi,nums[i]*mini)
            mini = min(nums[i], nums[i]* temp,nums[i]*mini)
            if maxi > ans:
                ans = maxi
            
        return ans
        
#         if len(nums) == 1: return nums[0]
#         @lru_cache(None)
#         def dp(ind, flag):
#             if ind == len(nums): return 1
            
#             if flag:
#                 if nums[ind] < 0:
#                     return min( nums[ind], nums[ind] * dp(ind + 1, True ),dp(ind + 1, True ))
#                 else: return min(nums[ind] ,nums[ind] * dp(ind + 1, False),dp(ind + 1, False))
#             else:
#                 if nums[ind] < 0:
#                     return max( nums[ind],nums[ind] * dp(ind + 1, True ),dp(ind + 1, True ))
#                 else: return max(nums[ind],nums[ind] * dp(ind + 1, False),dp(ind + 1, False))
#         return dp(0, False) solution has some bug
            

    
        