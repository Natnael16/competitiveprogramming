class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
#         3 5 4
        
#         0 0 4 
#         0 5  3 0 
        
#         3 2  
#         0 2
#         2 0
#         2 5
#         3 4
#         0 4
#         3 1
        if x + y < target: return False
        if target == 0: return True
        if x == 0:
            return y == target
        if y == 0:
            return x == target
        return not target % math.gcd(x,y)