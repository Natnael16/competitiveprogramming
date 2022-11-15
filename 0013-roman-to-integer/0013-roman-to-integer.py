class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        RtoI = {
        "I" : 1
        "V" : 5
        "X" : 10
        "L" : 50
        "C" : 100
        "D" : 500
        "M" : 1000 }
        
            if I and there is next and it is v or x sub 2 later
            if x and there is next and it is l or c sub 20 later
            if c and there is next and it is d or m sub 200 later
            else add them all from the map
            
        '''
        RtoI = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        tot = 0
        sub = 0
        for ind , r in enumerate(s):
            if r == "I" and ind + 1 < len(s) and (s[ind+1] == "V" or s[ind+1] == "X"):
                sub += 2
            elif r == "X" and ind + 1 < len(s) and (s[ind+1] == "L" or s[ind+1] == "C"):
                sub += 20
            elif r == "C" and ind + 1 < len(s) and (s[ind+1] == "D" or s[ind+1] == "M"):
                sub += 200
            tot += RtoI[r]
        tot -= sub
        return tot
            