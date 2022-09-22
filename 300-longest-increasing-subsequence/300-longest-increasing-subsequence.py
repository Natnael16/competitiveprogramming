class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # print(len(nums))
        @lru_cache(None)
        def solve(idx):
            if idx == len(nums) - 1: return 1
            g_elmts = []
            for i in range(idx , len(nums)):
                if nums[i] > nums[idx]: g_elmts.append(solve(i))
            if  not g_elmts: return 1
            # print(solve.cache_info())
            return max (g_elmts) + 1
        
        maxi =  - sys.maxsize
        for num in range(len(nums)):
            maxi = max(solve(num) , maxi)
        return maxi