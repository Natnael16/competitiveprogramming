class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        # catsanddog
        #    |
        len_s = len(s)
        self.ans = []
        wordSet = set(wordDict)
        def dp(ind,path):
            if ind >= len_s:
                self.ans.append(path.rstrip())
            cur_word = ""
            for i in range(ind , len_s):
                cur_word += s[i]
                if cur_word in wordSet:
                    dp(i+1,path + cur_word + " ")
                    
        dp(0,"")
        return self.ans
                    