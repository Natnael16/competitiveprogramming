class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for p in s:
            if not stack or p == '(':
                stack.append(p)
            elif stack[-1] == '(':
                stack.pop()
                stack.append(1)
            else:
                number = 0
                while stack and str(stack[-1]).isdigit():
                    number += stack.pop() 
                stack.pop()
                stack.append(number*2)
        return sum(stack)
        