#Natnael Tadele UGR/0415/12 sec 3


class Stack:
    def __init__(self) -> None:
        self.stack = []

    def getStack(self):
        return self.stack

    def push(self, s ):
        self.stack.append(s)
    
    def pop(self):
        return self.stack.pop()

    def peek(self):
        out = self.stack[-1]
        return out
    def isEmpty(self):
        return not self.stack


def isValid( s) -> bool:
    
    s = str(s)
    stack = Stack()
    pairs = { "(":")","[":"]","{":"}"}
    
    for char in s:
        if char in pairs:
            stack.push(char)
        elif char in pairs.values() and (not stack.isEmpty() and pairs[stack.peek()]) != char:
            return False
        elif ( not stack.isEmpty() and pairs[stack.peek()]) == char:
            stack.pop()
        else:
            continue
    if not stack.isEmpty(): return False
    return True
prompt = input('Enter a file name with the relative or absolute path(paths should be classified with forward slash):\n  ')
try:
    myfile = open("{}".format(prompt) , 'r')
    print(isValid(myfile.read()))
except:
    print("such file or directory doesn't exist")

