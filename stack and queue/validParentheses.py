class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = { ")":"(","]":"[","}":"{"}
        balanced = False
        try:
            for i in s:
                if str(i) in pairs.values():
                    stack.append(i)
                elif len(stack) != 0 and stack[-1] == pairs[i]:
                    stack.pop(-1)
                else:
                    stack.append(i)
        except KeyError:
            pass
        if len(stack) == 0:
            balanced=True
        return balanced