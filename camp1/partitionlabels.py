class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccurrance = {}
        for i in range(len(s)):
            lastOccurrance[s[i]] = i
        # print(lastOccurrance)
        left = 0
        right = len(s) - 1
        res = []
        while left < len(s):
            right = len(s) - 1
            while s[left] != s[right] and left < right:
                right -= 1
            if left == right:
                res.append(1)
                left += 1
            else:
                subleft = left + 1
                while subleft < right:
                    if lastOccurrance[s[subleft]] > right:
                        right = lastOccurrance[s[subleft]]
                    subleft += 1
                res.append(right - left + 1)
                    
                left = right + 1
        return res
