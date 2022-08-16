class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["@"] = {}
                

    def search(self, word: str) -> bool:
        node = self.root
        
        for ind , char in enumerate(word):
            if char in node and "@" in node[char]:
                node = node[char]
            else:
                return False
        return True
        
        
    def getNode(self):
        return self.root
        
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        tri = Trie()
        for word in words:
            tri.insert(word)
        
        ans = ""
        for word in words:
            sres = tri.search(word)
            if sres:
                if len(word) > len(ans):
                    ans = word
                elif len(word) == len(ans):
                    ans = min(ans, word)
        return ans
#         if not ans: return ""
        
#         ans.sort(reverse = True , key = lambda x : len(x))
#         i = 0
#         while i < len(ans) and len(ans[i]) == len(ans[0]):
#             i += 1

#         ans = sorted(ans[:i])
#         return ans[0]