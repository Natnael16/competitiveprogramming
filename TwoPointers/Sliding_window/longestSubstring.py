class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        my_set = set()
        res = 0
        i, j = 0, 0
        if len(s) == 1:
            return 1
        while j < len(s):
            if s[j] not in my_set:
                my_set.add(s[j])
                j += 1
                count += 1
                if res < count:
                    res = count
            else:
                if res < count:
                    res = count
                my_set.discard(s[i])
                count -= 1
                i += 1
        return res