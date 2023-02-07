class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        instructions = instructions * 4
        directions = [(0,1),(1,0),(0,-1) , (-1,0)] # up,  right , down, left
        cur_direction = 0
        cur_pos , initial =  (0, 0) ,(0, 0)
        for task in instructions:
            if task == "G":
                cur_x, cur_y = cur_pos
                d_x, d_y = directions[cur_direction % 4]
                cur_pos = (cur_x + d_x, cur_y + d_y)
            elif task == "L":
                cur_direction -=  1
            else:
                cur_direction +=  1
        return cur_pos == initial
        