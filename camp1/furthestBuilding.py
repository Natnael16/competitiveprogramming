class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        i = 0
        heap = []
        cur_pos = [bricks,ladders]
        while i < len(heights) - 1:
            diff = heights[i+1] - heights[i]
            if diff > 0:
                if diff <= cur_pos[0]:
                    heapq.heappush(heap,-diff)
                    cur_pos[0] -= diff
                    i += 1
                else:
                    if heap and -heap[0] > diff:
                        if cur_pos[1] > 0:
                            cur_pos[0] += (-heapq.heappop(heap))
                            cur_pos[1] -= 1
                        else:
                          
                            return i  
                    else:
                        if cur_pos[1] > 0:
                            cur_pos[1] -= 1
                            i+=1
                        else:
                            return i
            else:
                i += 1
        return i
