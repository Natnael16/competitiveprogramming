class Solution:
    def minOperations(self, logs: List[str]) -> int:
        up = 0
        for log in logs:
            if log == "../":
                if up > 0:
                    up -= 1
            elif log == "./":
                pass
            else:
                up += 1
        return up