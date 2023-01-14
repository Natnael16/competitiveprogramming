class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        for i , num_1 in enumerate(boxes):
            moves = 0
            for j , num_2 in enumerate(boxes):
                if num_2 == "1":
                    moves += abs(j - i)
            ans.append(moves)
        return ans
