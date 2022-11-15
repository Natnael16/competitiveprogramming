class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        spiral_order = [[rStart,cStart]]
        step = 1
        north_row_end = rStart
        north_col_end = cStart
        grid_size = rows * cols
        while len(spiral_order) < grid_size:
            east_row_end, east_col_end = self.move(north_row_end,north_col_end,step,spiral_order,rows,cols,"east")
            south_row_end, south_col_end = self.move(east_row_end,east_col_end,step,spiral_order,rows,cols,"south")
            step += 1
            west_row_end, west_col_end = self.move(south_row_end,south_col_end,step,spiral_order,rows,cols,"west")
            north_row_end, north_col_end = self.move(west_row_end,west_col_end,step,spiral_order,rows,cols,"north")
            step += 1
        return spiral_order
            
    def move(self,start_row,start_col,step,spiral_order,rows,cols,turn):
        for i in range(step):
            if turn == 'east':
                start_col += 1
            elif turn == 'west':
                start_col -= 1
            elif turn == 'south':
                start_row  += 1
            else:
                start_row -= 1
            is_bound = self.isBound(start_row,start_col,rows,cols)
            if is_bound:
                spiral_order.append([start_row,start_col])
                
        return [start_row,start_col]
    

    
    def isBound(self,row,col,row_bound,col_bound):
        return 0 <= row < row_bound and 0 <= col < col_bound