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
        
    def startsWith(self, prefix: str) -> bool:
        
        node = self.root
        # print(node , "s" , prefix)
        
        for ind , char in enumerate(prefix):
            if char in node:
                node = node[char]
            else:
                return False
        if len(node) == 1: return False
        return True
        
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words= list(set(words))
        trie = Trie()
        for word in words:
            trie.insert(word[::-1])
        
        count = 0
        for word in words:
            if not trie.startsWith(word[::-1]):
                count += (len(word) + 1)
        return count
            
            
                    