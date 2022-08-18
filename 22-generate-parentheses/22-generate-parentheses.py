class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
            def generate(out, )
            
        '''
        self.res = []
        def validP(arr):
            stack = []
            for b in arr:
                if b == "(":
                    stack.append(b)
                if b == ")":
                    if stack:
                        stack.pop()
                    else: return False
            return True if not stack else False
                
            
        def generate(out  , opening , closing , n):
            if len(out) == 2*n:
                if validP(out):
                    self.res.append("".join(out))
            if opening < n:
                out.append("(")
                generate(out,  opening + 1 ,closing , n)
                out.pop()
            if closing < n:
                out.append(")")
                generate(out,  opening ,closing + 1 , n)
                out.pop()
        generate([] , 0 , 0 , n)
        return self.res
            
                