class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur_dict = self.root
        for char in word:
            if char not in cur_dict:
                cur_dict[char] = {}
            cur_dict = cur_dict[char]
        cur_dict["."] = {}
        

    def search(self, word: str) -> bool:
        cur_dict = self.root
        for char in word:
            if char not in cur_dict:
                return False
            cur_dict = cur_dict[char]
        if "." in cur_dict:
            return True
        
            

    def startsWith(self, prefix: str) -> bool:
        cur_dict = self.root
        for char in prefix:
            if char not in cur_dict:
                return False
            cur_dict = cur_dict[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)