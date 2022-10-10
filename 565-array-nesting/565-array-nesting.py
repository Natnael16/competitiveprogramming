class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        seen = set()
        ans = -1
        def dfs(ind , count):
            nonlocal ans
            if ind in seen:
                ans = max(ans, count)
                return 
            seen.add(ind)
            next_ind = nums[ind]
            dfs(next_ind ,  count + 1)
        for i in range(len(nums)):
            dfs(i,0)
        return ans
            