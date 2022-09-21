class Solution:   
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        dirs = (0,1,0,-1,0)
        visited = set()
        inbound = lambda r ,c : 0<= r <len(image) and 0<= c < len(image[0])
        initial_c = image[sr][sc]
        def dfs(row ,col):
            visited.add((row, col))
            if image[row][col] == initial_c:
                image[row][col] = newColor
            for d in range(len(dirs) - 1):
                new_r = row + dirs[d]
                new_c = col + dirs[d + 1]
                if (new_r, new_c) not in visited and inbound(new_r, new_c) and image[new_r][new_c] == initial_c:
                    dfs(new_r, new_c)
        dfs(sr, sc)
        return image