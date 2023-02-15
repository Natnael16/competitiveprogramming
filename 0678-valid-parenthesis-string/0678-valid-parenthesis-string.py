class Solution:
    def checkValidString(self, s: str) -> bool:
        paranthesesCount=[0,0] 

        for c in s:
            if c=="(":
                paranthesesCount[0]+=1
                paranthesesCount[1]+=1
            elif c==")":
                paranthesesCount[0]-=1
                paranthesesCount[1]-=1
            else:
                paranthesesCount[0]-=1
                paranthesesCount[1]+=1
                
            if paranthesesCount[1]<0:
                return False
            
            paranthesesCount[0]=max(paranthesesCount[0], 0)
        if paranthesesCount[0]<=0:
            return True
        else:
            return False