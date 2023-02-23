class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        h1 = min(rec1[2],rec2[2]) - max(rec1[0],rec2[0])
        v2 = min(rec1[3],rec2[3]) - max(rec1[1],rec2[1])
        if h1 > 0 and v2 > 0:
            return True