class Solution:

    def removeDuplicateLetters(self, s: str) -> str:
        lastIndex = {}
        for i in range(len(s)):
            lastIndex[s[i]] = i
        # print(lastIndex)
        stack = []
        visited = set()
        for l in range(len(s)):
            if s[l] in visited: continue
            while stack and s[l] < stack[-1] and lastIndex[stack[-1]] > l:
                visited.remove(stack[-1])
                stack.pop()
                # print(stack)

            stack.append(s[l])
            visited.add(s[l])
        return ''.join(stack)