class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        tot_time = 0
        i = 0
        prev = None
        cur_sum = 0
        max_elem = -1
        while i < n:
            
            if not prev or colors[i] == prev:
                cur_sum += neededTime[i]
                max_elem = max(max_elem , neededTime[i])
                prev = colors[i]
            elif colors[i] != prev:
                tot_time += cur_sum - max_elem
                cur_sum = neededTime[i]
                max_elem = neededTime[i]
                prev = colors[i]
            i+=1
 
        tot_time += cur_sum - max_elem
        return tot_time