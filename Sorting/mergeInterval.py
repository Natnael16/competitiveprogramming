class Solution:

    def merge(self, li: List[List[int]]) -> List[List[int]]:
        li.sort(key=lambda s: s[1])
        j = 1
        while j < len(li):
            while j > 0 and (li[j - 1][0] in range(li[j][0], li[j][1] + 1)
                             or li[j - 1][1] in range(li[j][0], li[j][1] + 1)):
                li[j] = [min(li[j - 1][0], li[j][0]), li[j][1]]
                li.pop(j - 1)
                # print(li,j)
                j -= 1
            j += 1
        return li