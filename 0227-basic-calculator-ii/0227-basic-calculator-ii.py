class Solution:
    def format(self,s):
        s += "="
        formatted = []
        num = ""
        for char in s:
            if char != " ":
                if char.isdigit():
                    num += char
                else:

                    formatted.append(num)
                    formatted.append(char)
                    num = ""
        formatted.pop()
        return formatted
    def calculate(self, s: str) -> int:
        
        formatted = self.format(s)
        #do multiplications and division left to right
        stack = []
        for char in formatted:
            if stack and stack[-1] == "/":
                op  = stack.pop()
                first = stack.pop()
                stack.append(int(first)//int(char))
            elif stack and stack[-1] == "*":
                op  = stack.pop()
                first = stack.pop()
                stack.append(int(int(first)*int(char)))
            else:
                stack.append(char)
        stack2 = []
        for char in stack:
            if stack2 and stack2[-1] == "+":
                op  = stack2.pop()
                first = stack2.pop()
                stack2.append(int(first)+int(char))
            elif stack2 and stack2[-1] == "-":
                op  = stack2.pop()
                first = stack2.pop()
                stack2.append(int(int(first)-int(char)))
            else:
                stack2.append(char)
        return stack2[0]