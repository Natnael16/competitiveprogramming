class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []
        for left,right in intervals:
            if not stack:
                stack.append([left,right])
            else:
                peak_left , peak_right = stack[-1]
                if left > peak_right:
                    stack.append([left,right])
                else:
                    stack.pop()
                    stack.append([min(peak_left, left),max(peak_right,right)])
        return stack