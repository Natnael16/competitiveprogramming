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
            if char in node:
                node = node[char]
            else:
                return False
            if ind == len(word) - 1 and "@" not in node: return False
        return True
        
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for ind , char in enumerate(prefix):
            if char in node:
                node = node[char]
            else:
                return False
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)