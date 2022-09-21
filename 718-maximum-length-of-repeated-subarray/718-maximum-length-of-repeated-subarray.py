class Solution(object):
    def findLength(self, nums1, nums2):
        
        
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for a in range(len(nums1) - 1, -1, -1):
            for b in range(len(nums2) - 1, -1, -1):
                if nums1[a] == nums2[b]:
                    dp[a][b] = dp[a+1][b+1] + 1
        ans = -inf
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                ans = max(ans , dp[i][j])
        return ans