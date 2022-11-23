class Solution:
    @lru_cache(None)
    def minDistance(self,word1: str, word2: str,ind1= 0,ind2 = 0) -> int:
        if ind1 >= len(word1) and ind2 >= len(word2):
            return 0
        
        if ind1 >= len(word1):
            return len(word2[ind2:])
        if ind2 >= len(word2):
            return len(word1[ind1:])
        
        if word1[ind1] == word2[ind2]:
            return self.minDistance(word1, word2,ind1 + 1, ind2 + 1)
        
        add = self.minDistance( word1, word2,ind1 , ind2 + 1) + 1
        delete = self.minDistance( word1, word2,ind1 + 1, ind2) + 1
        replace = self.minDistance( word1, word2,ind1 + 1, ind2 + 1) + 1
        return min(add, delete, replace)