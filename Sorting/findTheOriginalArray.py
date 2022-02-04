from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        out = []
        changed.sort()
        countDict = Counter(changed)
        
        length = len(changed)
        if length % 2 != 0:
            return []
        i = length - 1 
        while i > 0:
            if countDict[changed[i]] == 0:
                i -= 1
            elif changed[i] % 2 != 0:
                return []
            else :
                countDict[changed[i]] -= 1
                countDict[changed[i]//2] -= 1
                out.append(changed[i]//2)
                i -= 1
        for i in countDict.values():
            if i != 0:
                return []
        return out