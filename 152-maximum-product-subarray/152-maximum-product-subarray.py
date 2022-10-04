class Solution:
    def maxProduct(self, nums: List[int]) -> int:
       
        prevMax = nums[0]
        prevMin = nums[0]
        ans = nums[0]

        for i in range(1,len(nums)):
            pMin,pMax = prevMin,prevMax       
            prevMin = min(nums[i],nums[i]*pMin,nums[i]*pMax)
            prevMax = max(nums[i],nums[i]*pMin,nums[i]*pMax)
            ans = max(prevMax,ans)

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
            

    
        