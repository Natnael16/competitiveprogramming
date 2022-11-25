class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        def cost(next_, curr, cars):
            curr_pos, curr_v = cars[curr]
            next_pos, next_v = cars[next_]
            
            if next_v >= curr_v:
                return float("inf")
    
            time = (next_pos - curr_pos) / (curr_v - next_v)
            return time
        
        answers = [float("inf")] * len(cars)
        stack = []
        for idx in reversed(range(len(cars))):
            while stack and cost(stack[-1], idx, cars) >= answers[stack[-1]]:
                stack.pop()
                
            if stack:
                answers[idx] = cost(stack[-1], idx, cars)
                
            stack.append(idx)
                
        for idx in range(len(answers)):
            if answers[idx] == float("inf"):
                answers[idx] = -1
                
        return answers