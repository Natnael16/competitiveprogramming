class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        j = 0
        i = 0
        while i < len(g) and j < len(s):
            if g[i] > s[j]:
                j += 1
            else:
                j += 1;count += 1;i += 1
        return count
                
                
                
                
            