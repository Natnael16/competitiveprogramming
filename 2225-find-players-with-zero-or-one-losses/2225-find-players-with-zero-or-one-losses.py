class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        wincount  = defaultdict(int)
        losecount = defaultdict(int)
        for win , lose in matches:
            wincount[win] += 1
            losecount[lose] += 1
            
        l1,l2 = [],[]
        for num in set(wincount | losecount):
            if num not in losecount:
                l1.append(num)
            elif losecount[num] == 1:
                l2.append(num)
        return [sorted(l1),sorted(l2)]