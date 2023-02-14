class Solution:
    def minimumDeletions(self, s: str) -> int:
    
        count = 0
        bCount = 0
        
        for char in s:
            if char == "a":
                count = min(bCount, count + 1)
            else:
                bCount += 1
        
        return count
                