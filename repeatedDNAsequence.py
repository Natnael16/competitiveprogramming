class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        left = 0
        right = 9
        if len(s) < 10:
            return []
        string_count = {}
        while right < len(s):
            if s[left:right + 1] in string_count:
                string_count[s[left:right + 1]] += 1
            else:
                string_count[s[left:right + 1]] = 0
            left += 1
            right += 1
        # print(string_count)
        res = []
        for c in string_count.keys():
              if string_count[c] >= 1:
                    res.append(c)
        return res
