"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        visited = dict()
        def dfs(node : 'Node' , parent : 'Node'):            
            if not node: return  
            
            new_node = Node(node.val,[])
            visited[node.val] = new_node
            parent.neighbors.append(new_node)
            
            for neigh in node.neighbors:
                
                if neigh and neigh.val not in visited:
                    dfs(neigh,new_node )
                elif neigh:
                    new_node.neighbors.append(visited[neigh.val])
        clone = Node(-1,[])
        
        dfs(node, clone)
        return clone.neighbors[0] if clone.neighbors else []
            
            
            