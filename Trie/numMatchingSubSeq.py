class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indexhash = defaultdict(list)
        tot_count = 0
        for i ,  w in enumerate(s):
                indexhash[w].append(i)
                
        for word in words:
            latest = -1
            count = 0
            for ch in word:
                if ch not in indexhash: break
                for j in indexhash[ch]:
                    # print(j)
                    if j > latest:
                        latest = j
                        count += 1
                        break
            if count == len(word):
               
                tot_count += 1
        return tot_count
                    





                    