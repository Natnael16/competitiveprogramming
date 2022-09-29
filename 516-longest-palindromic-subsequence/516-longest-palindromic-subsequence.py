class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        r = s[::-1]
        str_len = len(s)
        
        @lru_cache(None)
        def dp(p1, p2):
            if p1 >= str_len or p2 >= str_len:
                return 0
            if s[p1] == r[p2]:
                return 1 + dp(p1 + 1, p2 + 1)
            else:
                return max(dp(p1 + 1, p2), dp(p1, p2 + 1))
        return dp(0,0)
        
    