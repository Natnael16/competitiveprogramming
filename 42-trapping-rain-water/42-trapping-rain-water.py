class Solution:
    def trap(self, height: List[int]) -> int:
        '''         |
            |      
            | |  1
            |||
            collect if height has next greater(eq) element nearest and on which index
            collect that with mono stack
            [4,2,0,3,2,5]
            4 * 4 - ( 2 + 3,+ 2)
            16 - 7
            9
            2nd : 3rd
            
            [1,0,2]
            
        '''
        mono_stack = []
        next_greater = defaultdict(int)
        next_max = defaultdict(int)
        maxi = [-1,-1]
        for back in range(len(height)- 2 , - 1, -1):
            
            next_max[back] = max(maxi , [height[back + 1],back + 1])
            maxi = next_max[back]
        for ind, num in enumerate(height):
            while mono_stack and height[ind] >= height[mono_stack[-1]]:
                next_greater[mono_stack[-1]] = ind
                mono_stack.pop()
            mono_stack.append(ind)
        ptr = 0
        ans = 0
        while ptr < len(height):
            stick,nxt = 0,ptr+1
            if next_greater[ptr]:
                
                while nxt < next_greater[ptr]:
                    stick += height[nxt]
                    nxt += 1
                ans += min(height[ptr] , height[next_greater[ptr]]) * (next_greater[ptr] - ptr - 1) - stick
                ptr = next_greater[ptr]
            elif next_max[ptr]:
                while nxt < next_max[ptr][1]:
                    stick += height[nxt]
                    nxt += 1
                ans += min(height[ptr],next_max[ptr][0]) * (next_max[ptr][1] - ptr - 1) - stick
                ptr = next_max[ptr][1]
            else:
                ptr += 1
                

        return ans
                    
                    
                    
                    
                    
            
        