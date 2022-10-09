class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ad_list = defaultdict(list)
        visited = set()
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                ad_list[pattern].append(word)
        
        q = deque([(beginWord,1)])
        
        while q:
            cur,moves = q.popleft()
            if cur == endWord:
                return moves
                
            visited.add(cur)
            patterns = [cur[:i] + '*' + cur[i + 1:] for i in range(len(cur))]
            
            for pattern in patterns:
                neighbors = ad_list[pattern]
                
                for neigh in neighbors:
                    if neigh not in visited:
                        q.append((neigh,moves + 1))
        return 0

        
        
        
        
        
            
        