class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for ind in range(len(s)):
            if not stack or s[ind] == "(":
                stack.append(ind)
            elif s[stack[-1]] == "(" and stack[-1] != -1:
                stack.pop()
                max_len = max(max_len, ind - stack[-1])
            else:
                stack.append(ind)
        return max_len
            
                