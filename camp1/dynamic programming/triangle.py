class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        in_bound = lambda idx: idx[0] + 1 < len(triangle)
        cache = {}

        def recur(parent_idx):
            if not in_bound(parent_idx):
                return triangle[parent_idx[0]][parent_idx[1]]
            if parent_idx in cache: return cache[parent_idx]
            print(parent_idx)
            left = recur((parent_idx[0] + 1, parent_idx[1]))
            cache[(parent_idx[0] + 1, parent_idx[1])] = left
            right = recur((parent_idx[0] + 1, parent_idx[1] + 1))
            cache[(parent_idx[0] + 1, parent_idx[1] + 1)] = right
            cache[parent_idx] = min(
                left, right) + triangle[parent_idx[0]][parent_idx[1]]
            return cache[parent_idx]

        return recur((0, 0))
