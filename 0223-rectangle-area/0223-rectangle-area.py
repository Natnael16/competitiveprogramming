class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
#         if they dont intersect the answer is gonna be addition of the two areas
        
#         A1 + A2 - intersection(A1 A2)
        areaA = (ax2 - ax1) * (ay2 - ay1)
        areaB = (bx2 - bx1) * (by2 - by1)
        
        overlap_height = min(ay2, by2) - max(ay1,by1)
        overlap_width = min(ax2,bx2) - max(ax1,bx1)
        overlap_area = overlap_height * overlap_width
        return areaA + areaB  - (overlap_area if overlap_height > 0 and overlap_width > 0 else 0)
        
        