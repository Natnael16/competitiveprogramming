class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for ind,  char in enumerate(s):
            if counter[char]==1:
                return ind
        return -1