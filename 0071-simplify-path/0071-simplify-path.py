class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for chunk in path:
            if stack and chunk == "..":
                stack.pop()
            elif chunk and chunk != "." and chunk != "..":
                stack.append(chunk)

        return "/" + "/".join(stack)
