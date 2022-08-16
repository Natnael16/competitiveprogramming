class Trie:
    
    def __init__(self):
        self.root = {}
        
    def insert(self , word):
        node = self.root
        dirs = word.split("/")[1:]
        for dir_ in dirs:

            if "@" in node: return False
            if dir_ not in node:
    
                node[dir_]= {}
            node = node[dir_]
        node["@"] = {}
        return True
        

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        trie = Trie()
        out = []
        for dir_ in folder:
            if trie.insert(dir_): out.append(dir_)
        return out