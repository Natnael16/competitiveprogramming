class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0 
        j = len(height) - 1
        out = 0
        while i != j:
            shorter = min(height[i],height[j])
            area = shorter*abs(j-i)
            if area > out:
                out = area
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
                
        return out