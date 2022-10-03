class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # catsandog
        #   |
        #top_down
        
#         wordset = set(wordDict)
#         @lru_cache(None)
#         def dp(ind):
#             if ind == len(s): return True
            
#             word = []
#             flag = False
#             for i in range(ind,len(s)):
#                 word.append(s[i])
#                 if "".join(word) in wordset:
#                     flag = flag or dp(i + 1)
#             return flag
#         return dp(0)

        n = len(s)
        wordset = set(wordDict)
        dp = [False] * (n + 1)
        dp[-1] = True
        
        for i in range(n-1,-1,-1):
            queue = deque([])
            for j in range(i,-1,-1):
                queue.appendleft(s[j])
                if "".join(queue) in wordset and dp[i + 1]:
                    dp[j] = True
        return dp[0]
        
        
        
    
    
        