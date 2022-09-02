class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        nearest_left = defaultdict(int)
        nearest_right = defaultdict(int)

        set_heater = set(heaters) 

        positions = houses + heaters 
        positions.sort() 
        
        nearest_left_heater = None
        for h in positions: 
            if h in set_heater:
                nearest_left_heater = h
            nearest_left[h] = nearest_left_heater
          
          
        nearest_right_heater = None 
        for ind in range(len(positions) - 1,-1,-1):
            if positions[ind] in set_heater:
                nearest_right_heater = positions[ind]
            nearest_right[positions[ind]] = nearest_right_heater
          
    
        maxi= -inf
        for house in houses: 
            left = nearest_left[house]
            right = nearest_right[house]
            if left and right:
                mini = min(abs(house - left), abs(house - right))
                maxi = max(maxi, mini)
            elif left:
                maxi = max(abs(house - left) , maxi)
            elif right:
                maxi = max(abs(house - right) , maxi)
            
        return maxi