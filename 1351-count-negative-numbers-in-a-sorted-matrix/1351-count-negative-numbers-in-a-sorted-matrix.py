class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:         
        # [[4,3,2,-1],
        #  [3,2,1,-1],
        #  [1,1,-1,-2],
        #  [-1,-1,-2,-3]]
        n , m = len(grid) , len(grid[0])
        row, col= [n - 1,0]
        count = 0
        while  0<= row < n and 0 <= col < m:
            if grid[row][col] < 0:
                count += m - col
                row -= 1
            else:
                col += 1
        return count
            
        
            