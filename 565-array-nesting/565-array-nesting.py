class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        ans = -1
        def dfs(ind , count):
            nonlocal ans
            if nums[ind] == -1:
                ans = max(ans, count)
                return 
            
            next_ind = nums[ind]
            nums[ind] = -1
            dfs(next_ind ,  count + 1)
        for i in range(len(nums)):
            if nums[i] != -1:
                dfs(i,0)
        return ans
            