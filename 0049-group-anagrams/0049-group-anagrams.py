class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        sorted_unsorted = defaultdict(list)
        for cand in strs:
            sorted_unsorted["".join(sorted(cand))].append(cand)
        for s_uns in sorted_unsorted:
            anagrams.append(sorted_unsorted[s_uns])
        return anagrams