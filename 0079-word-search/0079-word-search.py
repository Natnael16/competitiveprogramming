class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dist = 0
        for w in range(len(word)//2):
            if word[w] != word[w+1]:
                dist +=1
        back = 0
        for w in range(len(word)//2 + 1,len(word) -1):
            if word[w] != word[w+1]:
                back +=1
        if dist < back:
            word = word[::-1]
            
        n,m=len(board),len(board[0])
        inbound = lambda x,y : 0<= x < n and 0<= y < m
        dirs = (0,1,0,-1,0)
        self.visited = set()
        def dfs(row, col,path,match_ind):
            if len(path) == len(word):
                if "".join(path) == word:
                    return True
                return False
            if match_ind > len(word):
                return False
            if word[match_ind] != path[match_ind]:
                return False
            flag = False
            for d in range(4):
                new_row, new_col = row + dirs[d], col + dirs[d+1]
                if inbound(new_row, new_col) and (new_row, new_col) not in self.visited:
                    self.visited.add((new_row, new_col))
                    path.append(board[new_row][new_col])
                    flag = flag or dfs(new_row,new_col,path,match_ind + 1)
                    self.visited.remove((new_row, new_col))
                    path.pop()
            return flag
                
        for row in range(n):
            for col in range(m):
                self.visited.add((row,col))
                if board[row][col] == word[0]:
                    if dfs(row, col,[board[row][col]],0):
                        return True
                self.visited.remove((row,col))
  