from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = []
        length = len(arr)/2
        counter  = Counter(arr)
        key = list(counter.keys())
        for i in key:
            count.append((i,counter[i]))
        arranged = sorted(count,key=lambda j:j[1],reverse = True)
        inc = 1
        store = 0
        for i in arranged:
            store += i[1]
            if store < length:
                inc += 1
        return inc