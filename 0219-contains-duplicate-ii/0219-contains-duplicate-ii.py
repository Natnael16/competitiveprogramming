class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_dict = defaultdict(list)
        
        for idx , num in enumerate(nums):
            index_dict[num].append(idx)
        
        for key in index_dict:
            index_array = index_dict[key]
            for idx in range(1,len(index_array)):
                if index_array[idx] - index_array[idx-1] <= k:
                    return True
        return False
        