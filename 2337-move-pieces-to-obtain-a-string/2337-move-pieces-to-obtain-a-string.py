class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        if start.replace("_","") != target.replace("_", ""):
            return False
        
        st ,tar, length = 0 ,0 ,len(start)
        while st < length and tar < length:
            while st < length and start[st] == "_":
                st += 1
            while tar < length and target[tar] == "_":
                tar += 1
            if st >= length or tar >= length:
                break
                
            if start[st] == "L" and st < tar:
                return False
            if start[st] == "R" and st > tar:
                return False
            
            st += 1
            tar += 1
        return True
        
        
        
        
        