class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Solution:
    def __init__(self):
        self.root = Node()
        
    def add(self , word):
        node = self.root
        for ch in word:
            if not ch in node.children: node.children[ch] = Node()
            node = node.children[ch]
            
        node.isEnd = True
        
    def search(self, word):
        res = []
        node = self.root
        
        for w in range(len(word)):
            if not word[w] in node.children: return
            # if node.isEnd:
            #     print(word[:w+1])
            #     heappush(res , word[:w + 1])
            # this was the big problem I encountered solving this problem
            
            node = node.children[word[w]]
        q = [(node, word)]

        while q:
            cur_node, parent = q.pop()
            if cur_node.isEnd: heappush(res , parent)
            for child in cur_node.children:
                q.append((cur_node.children[child] , parent + child))
                
        new = []
        if len(res) > 3:
            for _ in range(3): new.append(heappop(res))
            new.sort()
            return new
        else:
            
            res.sort()
            return res
        
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        final = []
        for product in products:
            self.add(product)
        
        
        for ind in range(len(searchWord)):
        
            final.append(self.search(searchWord[:ind+1]))
        # print(final)
        return final