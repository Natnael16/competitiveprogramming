class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        counter = Counter(changed)
        zcount = counter[0]
        
        changed.sort()
        ans = []
        if zcount % 2 == 0:
            for i in range(zcount//2):
                ans.append(0)
        else: return []
        
        counter[0] = 0
        for num in changed:
            if counter[num] < 1: continue
            counter[num] -= 1
            double = 2 * num
            if double in counter and counter[double] > 0:
                counter[double] -= 1
                ans.append(num)
            else: return []
        return ans