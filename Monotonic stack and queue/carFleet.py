class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tup_li=[]
        for i in range(len(position)):
            tup_li.append([position[i], speed[i]])
        tup_li.sort(key= lambda n:n[0], reverse= True)
        mono_stack = []
        for i in tup_li:
            if len(mono_stack) == 0:
                mono_stack.append(i)
            elif len(mono_stack) > 0:
                timeOfi = (target - i[0])/i[1]
                timeOfstk = (target - (mono_stack[-1])[0])/(mono_stack[-1])[1]
                while timeOfi <= timeOfstk:
                    mono_stack[-1][0] = max(i[0],mono_stack[-1][0])
                    mono_stack[-1][1] = min(i[1],mono_stack[-1][1])
                    break
                if timeOfi > timeOfstk:
                    mono_stack.append(i)
        return len(mono_stack)