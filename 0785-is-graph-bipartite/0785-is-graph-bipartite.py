class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        set1 ,set2 = set(), set()
        for i in range(len(graph)):
           
            if i in set1 or i in set2: continue
            
            q = deque([(i,0,set1, set2)])
            while q:
                node,turn , s1, s2 = q.popleft()
                if not turn:
                    s1.add(node)
                else:
                    s2.add(node)
                    
                for neigh in graph[node]:
                    if not turn:
                        if neigh in s1:
                            
                            return False
                        if neigh not in s2:
                            q.append((neigh , 1- turn,s1,s2))
                        
                    else:
                        if neigh in s2:
                            
                            return False
                        if neigh not in s1:
                            q.append((neigh , 1- turn,s1,s2))
        
        return True
                            
                