class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        colors = defaultdict(lambda : -1)
        
        def dfsColor(node, cur_color):
            colors[node] = cur_color
            truth = True
            for neigh in graph[node]:
                if colors[neigh] == 0 or colors[neigh] == 1:
                    colors[node] = 1
                    truth = False
                elif colors[neigh] == -1:
                    truth = truth and dfsColor(neigh,0)
            
                    
            if truth and colors[node] != 1:
                colors[node] = 2
            else:
                colors[node] = 1
            return truth
        
        
        for node in range(len(graph)):
            if colors[node] == -1:
                dfsColor(node,0)
                
      
        
        answerList = []
        
        for node in colors:
            if colors[node] == 2:
                answerList.append(node)
        return sorted(answerList)
            
            
            
            
        