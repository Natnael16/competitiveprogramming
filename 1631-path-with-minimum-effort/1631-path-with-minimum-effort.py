class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows,cols = len(heights), len(heights[0])
        directions = [(0,1), (1,0),(-1,0),(0,-1)]
        def inbound(row,col):
            return 0 <= row < rows and 0 <= col < cols 
      
        visited = set()
        heap = [(0,(0,0))]
        count = 0
        while heap:
            count += 1
  
            cur_dif , node = heappop(heap)
    
            row, col = node
            if (row, col) in visited:continue
            if node == (rows-1,cols-1):
                return cur_dif
            visited.add((row, col))
            for add_row, add_col in directions:
                new_row, new_col = row + add_row, col + add_col
                if (new_row, new_col) not in visited and inbound(new_row, new_col):
                    next_diff = abs(heights[row][col] - heights[new_row][new_col])
                    heappush(heap, (max(cur_dif,next_diff),(new_row,new_col)))
                    
                    
                
                
        
        