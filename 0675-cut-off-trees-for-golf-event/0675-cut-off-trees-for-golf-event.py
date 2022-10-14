from sortedcontainers import SortedList
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        
        self.count=0
        dirs = (1,0,-1,0,1)
        n,m = len(forest),len(forest[0])
        def bfs(row,col,target):
            q=deque([(row,col,0)])
            seen = [[False] * m for _ in range(n)]
            seen[row][col] = True
            while q:
                cur_r,cur_c, step = q.popleft()
                if forest[cur_r][cur_c] == target:
                    forest[cur_r][cur_c] = 1
                    self.count += step
                
                    return (cur_r,cur_c)
                    
                for d in range(4):
                    new_r,new_c = cur_r + dirs[d],cur_c + dirs[d+1]
                    if 0 <= new_r < n and 0 <= new_c < m and forest[new_r][new_c] and not seen[new_r][new_c]: 
                        seen[new_r][new_c] = True
                        q.append((new_r,new_c,step+1))
          
            return -1
        
        heap = SortedList()
        for row in range(n):
            for col in range(m):
                if forest[row][col] > 1:
                    heap.add(forest[row][col])
        p = 0
        next_pos = (0,0)
        while p < len(heap):
            next_pos = bfs(next_pos[0],next_pos[1],heap[p])
            p += 1
            if next_pos == -1: return -1
        return self.count
            
            
            