class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if len(stack)==0:
                stack.append(i)
            elif len(stack)>0:
                while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                    sub = stack[-1]
                    app = i - sub
                    out[sub] = app
                    stack.pop()
                stack.append(i)
        return out