class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ''' ,         1
        tar = 4     tar = 3
        1111          1111
        1   -1
      tar = 3 tar-5
                
    111         111
    base if ind > nums.length: return 0
    
        if ind == nums.length and tar == 0: 
            return 1
        
        return recur(ind + 1 , tar - nums[ind]) + recur(ind + 1 ,tar +nums[ind])
    
        '''
        @lru_cache(None)
        def dp(ind , target):
            if ind == len(nums):
                if target == 0: return 1
                else: return 0

            return dp(ind + 1 , target - nums[ind]) + dp(ind + 1 , target + nums[ind])
        return dp(0 , target)
        '''
        time complexity if memoized O(len(nums) * target) == O(20 * 2000)
        '''
        