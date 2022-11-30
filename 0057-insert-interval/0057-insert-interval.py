class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insertpos = bisect_right(intervals,newInterval)
        intervals.insert(insertpos,newInterval)
        
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
                
        