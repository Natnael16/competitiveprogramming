class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opp = ["+","-","*","/"]
        stack = []
        for i in tokens:
            if i not in opp:
                stack.append(int(i))
            elif i in opp:
                a2= stack.pop()
                a1 = stack.pop()
                if i == "+":
                    val = a1 + a2
                elif i == "-":
                    val = a1 - a2
                elif i == "*":
                    val = a1 * a2
                elif i == "/":
                    val = math.trunc(a1 / a2)
                    
                stack.append(val)
        return stack.pop()