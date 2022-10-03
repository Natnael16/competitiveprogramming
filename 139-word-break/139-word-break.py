class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # catsandog
        #   |
        wordset = set(wordDict)
        @lru_cache(None)
        def dp(ind):
            if ind == len(s): return True
            
            word = []
            flag = False
            for i in range(ind,len(s)):
                word.append(s[i])
                if "".join(word) in wordset:
                    flag = flag or dp(i + 1)
            return flag
        return dp(0)
        