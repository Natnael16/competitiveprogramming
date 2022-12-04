class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        zero_indicies = deque()
        directions = [[0,1],[1,0], [0,-1],[-1,0]]
        rows, cols = len(mat), len(mat[0])
        mat_copy = [[inf] * cols for _ in range(rows)]
        
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    zero_indicies.append((row,col))
        level = 1
        visited = set()
        while zero_indicies:
            q_length = len(zero_indicies)
            for _ in range(q_length):
                cur_row, cur_col = zero_indicies.popleft()
                visited.add((cur_row,cur_col))
                for ch_row, ch_col in directions:
                    new_row, new_col = ch_row + cur_row, ch_col + cur_col
                    if 0 <= new_row < rows and 0 <= new_col < cols and mat[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                        mat_copy[new_row][new_col] = min(mat_copy[new_row][new_col] , level)
                        zero_indicies.append((new_row,new_col))
            level += 1
        for row in range(rows):
            for col in range(cols):
                if mat_copy[row][col] == inf:
                    mat_copy[row][col] = 0
        return mat_copy
            