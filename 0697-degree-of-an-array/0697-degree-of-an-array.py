class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counter = Counter(nums)
        sorted_counter = sorted(counter, key=lambda x : (counter[x]), reverse=True)
        indicies = defaultdict(list)
        for index , num in enumerate(nums):
            indicies[num].append(index)
        target_count = counter[sorted_counter[0]]
        min_size = inf
        for cand in sorted_counter:
            if counter[cand] == target_count:
                min_size = min(min_size, indicies[cand][-1] - indicies[cand][0] + 1)
            else:
                break
        
        
        return min_size