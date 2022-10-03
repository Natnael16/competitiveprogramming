class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''0 0
      10  11
    20  21  22 
  30  31  32  33 ''' 
    # row + 1,col -left
    # row + 1, col + 1 - right
        grid=[[1]]
        shift = 2
        for row in range(numRows-1):
            col = [0] * shift
            grid.append(col)
            for c in range(row + 1):
                grid[row+1][c] += grid[row][c]
                grid[row + 1][c + 1] += grid[row][c]
            shift += 1
        return grid
            
    