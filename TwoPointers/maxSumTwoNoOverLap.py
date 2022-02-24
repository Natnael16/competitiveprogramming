class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        i, j = 0 , firstLen - 1
        x, y= 0 , secondLen -1
        di1 = {}
        di2 = {}
        while j < len(nums) or y < len(nums):
            if j < len(nums):
                di1['{} {}'.format(i,j)] = sum(nums[i:j+1])
            if y < len(nums):
                di2['{} {}'.format(x,y)] = sum(nums[x:y+1])
            i += 1
            j += 1
            x += 1
            y += 1
        p, m = 0 , 0
        maxS = 0
        k1 = list(di1.keys())
        k2 = list(di2.keys())
        while p < len(k1) or m < len(k2):
            if m >= len(k2):
                break
            if p < len(k1):
                if (int(k2[m].split()[0]) <= int(k1[p].split()[0]) <= int(k2[m].split()[1])) or (int(k2[m].split()[0]) <= int(k1[p].split()[1]) <= int(k2[m].split()[1])) or (int(k1[p].split()[0]) <= int(k2[m].split()[0]) <= int(k1[p].split()[1])) or (int(k1[p].split()[0]) <= int(k2[m].split()[1]) <= int(k1[p].split()[1])):
                    p += 1
                    continue
                else:
                    if maxS < di1[k1[p]] + di2[k2[m]]:
                        maxS = di1[k1[p]] + di2[k2[m]]
                    p += 1
            else:
                p = 0
                m += 1
        
        return maxS