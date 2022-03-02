class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  newColor: int) -> List[List[int]]:
        Row, Col = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image

        # inbound = lambda row, col: 0 <= row < len(image) and 0 <= col < len(image[0])
        def dfs(new_row, new_col):
            if image[new_row][new_col] == color:
                image[new_row][new_col] = newColor
                if new_row >= 1: dfs(new_row - 1, new_col)
                if new_row + 1 < Row: dfs(new_row + 1, new_col)
                if new_col >= 1: dfs(new_row, new_col - 1)
                if new_col + 1 < Col: dfs(new_row, new_col + 1)

        dfs(sr, sc)
        return image