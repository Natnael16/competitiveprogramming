class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words_set = set(words) # Time Complexity O(N)
        
        cache = defaultdict(int)
        @lru_cache(None)
        def dp(word):
            
            maxLength = 1
            
            for i in range(len(word)): 
                new_word = word[:i]+word[i+1:]
                if new_word in words_set:
                    currenLength = 1 + dp(new_word)
                    maxLength = max(maxLength, currenLength)
            
            return maxLength
        
        max_chain = 1
        for word in words:
            max_chain = max(max_chain, dp(word))
        
        return max_chain