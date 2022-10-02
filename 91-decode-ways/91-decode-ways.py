class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dp(ind):
            if ind >= len(s): return 1
            elif ind == len(s) - 1 and s[ind] != "0": return 1
            elif s[ind] == "0": return 0
          
            if 0 <= int(s[ind:ind + 2]) < 27:
                return dp(ind + 1) + dp(ind + 2)
            else:
                return dp(ind + 1)
        return dp(0)
         
        