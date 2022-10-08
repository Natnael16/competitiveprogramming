class Solution:
    def totalNQueens(self, n: int) -> int:
        rows = set()
        cols = set()
        sums= set() # for diagonals
        diff = set() #for diagonals
        
        #return true if spot can place Queens else False
        def isAvailable(row,col):

            if (row in rows) or (col in cols) or (row + col in sums) or (row - col in diff): return False
            return True
        
        self.ans = []
        def backtrack(queen,row,path):
            if row == n and not queen:
                self.ans.append(list(path))
            elif row == n and queen > 0: return
            
            for col in range(n):
                if isAvailable(row,col): # If Spot it is not available in column we do nothing 
                    column = ["."] * n
                    column[col] = "Q"
                    path.append("".join(column))
                    rows.add(row)
                    cols.add(col)
                    sums.add(row + col)
                    diff.add(row - col)
                    
                    backtrack(queen - 1,row + 1,path)
                    
                    path.pop()
                    rows.remove(row)
                    cols.remove(col)
                    sums.remove(row + col)
                    diff.remove(row - col)
                    
        backtrack(n,0,[])
        return len(self.ans)