import sys 
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        decreasing = [0] * len(security)
        increasing = [0] * len(security)
        prev = sys.maxsize
        psum = -1 
        for dec in range(len(security)):
            if security[dec] <= prev:
                psum += 1
                decreasing[dec] = psum

            else:
                psum = 0
            prev = security[dec]
        prev = sys.maxsize
        psum = -1
        for inc in range(len(security) - 1 , -1 , -1 ):
            if security[inc] <= prev:
                psum += 1
                increasing[inc] = psum
                
            else:
                psum = 0
            prev = security[inc]
#         print(increasing)
        
#         print(decreasing)
        result = []
        for ind ,  sec in enumerate(security):
            if ind - time >= 0 and - time + decreasing[ind] >= 0 and  - time + increasing[ind] >= 0 :
                result.append(ind)
        return result
                