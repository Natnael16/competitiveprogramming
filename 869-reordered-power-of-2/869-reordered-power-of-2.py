class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count = Counter(str(n))
        for b in range(31):
            if count == Counter(str(1 << b)): return True
            
        