class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        
        ls = len(stamp) 
        lt = len(target)
        targlist = list(target)
        ans = []
        
        remain = lt
        def check(ptr):
            flag = False
            for i in range(ls):
                if targlist[ptr + i] == "?":
                    continue
                flag = True
                if targlist[ptr + i] != stamp[i]:
                    return False
            return flag
                    
        while remain > 0:
            flag = False
            for ind in range(lt - ls + 1):
                if check(ind):
                    ans.append(ind)
                    flag = True
                    for j in range(ls):
                        if targlist[j +  ind]!= "?":
                            targlist[j + ind] = "?"
                            remain -= 1
                    
            if not flag: return []
        return ans[::-1]
    
            
        