class Solution:
    def minimumBuckets(self, street: str) -> int:
        # 1 check if imposible
        if street.find("HHH") != -1: return -1
        if street.startswith("HH") or street.endswith("HH"): return -1
        
        street = list(street)
        
    
        count = 0
        # add in H.H
        if len(street) == 1:
            return -1 if street[0] == "H" else 0
        if len(street) == 2:
            if street[0] == street[1] == ".":
                return 0
            else: return 1
            
            
        # for len >= 3
        for i in range(1 , len(street)-1):
            if street[i-1] == "H" and street[i] == '.' and street[i+1] == "H":
                street[i-1] , street[i+1] , street[i] = "N" , "N" , "B"
                count += 1
        
        # add in the rest places
        count += street.count("H")
        
        return count