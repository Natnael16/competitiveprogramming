
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = []
        arranged = sorted(nums)
        count = 0
        i = 0
        if len(nums) > 1:
            while i < len(arranged)-1:
                count = 1
                while arranged[i] == arranged[i+1]:
                    count += 1
                    i+=1
                    if i >= len(arranged)-1:
                        break
                counter.append([arranged[i],count])
                i+=1
                if i >= len(arranged)-1:
                    break
            if arranged[-1] != arranged[-2]:
                counter.append([arranged[-1],1])
        else:
            counter.append([nums[0],1])
        out = sorted(counter,key = lambda x : x[1],reverse = True)
        retu = []
        for i in range(k):
            retu.append(out[i][0])
        return retu