from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        edges = []
        
        for left , right, height in buildings:
            edges.append((left, -height, 0))
            edges.append((right, height , 1))
        edges.sort()
        ans = []
        heights = SortedList([0])
        for x, h, turn in edges:
            if turn == 0:
                heights.add(h)
            else:
                heights.remove(-h)
            if not ans or -ans[-1][1] != heights[0]:
                ans.append([x,-heights[0]])
        return ans