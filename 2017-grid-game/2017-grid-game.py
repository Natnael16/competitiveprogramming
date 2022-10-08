''' DP approach That doesn't Work '''
# class Solution:
#     def gridGame(self, grid: List[List[int]]) -> int:

#         row_len , col_len = 2 , len(grid[0])
        
#         # construct a grid to know where to choose from right or down
#         def constructGrid(matrix):
#             dp = [[0] * col_len for _ in range(2)]
#             psum = 0
#             for back in range(col_len-1,-1,-1):
#                 psum += matrix[1][back]
#                 dp[1][back] = psum
                
#                 dp[0][back] = matrix[0][back] +  max(dp[1][back], dp[0][back + 1] if back + 1 < col_len else 0)
#             return dp
            
#         dp = constructGrid(grid)
        
#         # make zero the original grid based on the constructed grid
#         row ,col = 0, 0
#         while row < 2 and col < col_len:
            
#             grid[row][col] = 0
#             if row + 1 < row_len and col + 1 < col_len:
#                 if dp[row + 1][col] >= dp[row][col + 1]:
#                     row += 1
#                 else:
#                     col += 1
#             elif row + 1 >= row_len: col+=1
#             elif col + 1 >= col_len: row+=1
                
#         dp = constructGrid(grid)
        
#         return dp[0][0]

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        col_len = len(grid[0])
        top_sum = sum(grid[0])
        bottom_sum = 0
        ans = inf
        for col in range(col_len):
            top_sum -= grid[0][col]
            ans = min(ans , max(top_sum, bottom_sum))
            bottom_sum += grid[1][col]
        return ans
        
        
                
            
        
            