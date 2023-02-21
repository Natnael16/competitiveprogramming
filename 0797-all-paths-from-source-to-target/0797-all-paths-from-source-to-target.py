class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        final_path = []
     
        self.getPaths(0,[],final_path,graph)
        return final_path
    
    def getPaths(self,node, temp_path, final_path, graph):
        if node == len(graph) - 1:
            temp_path.append(node)
            final_path.append(temp_path[:])
            temp_path.pop()
            return
        for neigh in graph[node]:
            temp_path.append(node)
            self.getPaths(neigh, temp_path, final_path, graph)
            temp_path.pop()
            