class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cur_capacity = capacity
        steps = 0
        cur_pos = -1
        while cur_pos!= len(plants) - 1 :
            if cur_pos + 1 < len(plants) and plants[cur_pos + 1] <= cur_capacity:
                steps += 1
                cur_pos += 1
                cur_capacity -= plants[cur_pos]
            else:
                steps += (cur_pos + 1)*2
                cur_capacity = capacity
        return steps