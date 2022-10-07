class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        def isValid(s):
            stack = []
            for i in s:
                if i == "(":
                    stack.append(i)
                elif not stack:
                    return False
                elif stack[-1] == "(":
                    stack.pop()
            return True if not stack else False
                        
        def backtrack(open_count , close_count, path):
            if open_count == 0 and close_count == 0:
                if isValid(path):
                    self.ans.append(path)
                return
            if open_count:
                backtrack(open_count - 1,close_count,path+'(')
            if close_count:
                backtrack(open_count,close_count-1,path+")")
        backtrack(n,n,"")
        return self.ans