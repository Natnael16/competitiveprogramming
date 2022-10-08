class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        rows = {0,1}
        cols = {1,3}
        sums={1,4}
        diff = {-1,-2}
        
        . Q . .
        . . . Q 
        Q . . .
        . . Q .
        
        q = 1, row = 4 cols = 4  satisfied rows and cols length but q has to be 0
        
        q = 0 row = 4 cols = 4 add the grid
        00 01 02 03
        10 11 12 13
        20 21 22 23
        30 31 32 33
        '''
        
        rows = set()
        cols = set()
        sums= set()
        diff = set()
        def isAvailable(row,col):
            #return true if spot can place Queens else False
            if (row in rows) or (col in cols) or (row + col in sums) or (row - col in diff): return False
            return True
        self.ans = []
        def backtrack(queen,row,path):
            if row == n and not queen:
                self.ans.append(list(path))
            elif row == n and queen > 0: return
            
            for col in range(n):
                if isAvailable(row,col):
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
        return self.ans
                    
            
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        