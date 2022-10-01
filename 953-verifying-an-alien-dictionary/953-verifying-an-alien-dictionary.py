class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_dict = {}
        for i in range(len(order)):
            alien_dict[order[i]] = i
        for ind in range(len(words) - 1):
            word1 , word2 = words[ind], words[ind + 1]
            
            i = 0
            while i < len(word1):
                if i >= len(word2): return False
                if alien_dict[word1[i]] > alien_dict[word2[i]]:
                    return False
                elif alien_dict[word1[i]] == alien_dict[word2[i]]:
                    i+= 1
                else: break
        return True