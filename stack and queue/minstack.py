class Stack:

    def __init__(self):
        self.stack = []
        
    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def top(self):
        out = self.stack[-1]
        return out

            


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# (){}({}))competitiveprogramming-week-1-sorting-\stack and queue\minstack.py