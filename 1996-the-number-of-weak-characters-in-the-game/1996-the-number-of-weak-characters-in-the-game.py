class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x : (x[0], -x[1]))
        # the last is always non weak after sorting
        
        mono_stack = []
        count = 0
        for attack , defence in properties:
            while mono_stack and mono_stack[-1][0] < attack and mono_stack[-1][1] < defence:
                mono_stack.pop()
                count += 1
            mono_stack.append((attack, defence))
        return count