class Solution:
    def robotWithString(self, s: str) -> str:
        stack = []
        right_min = defaultdict(tuple)
        smallest = (s[-1], len(s) - 1)
        right_min[len(s) - 1] = ("zz", len(s))
        for back in range(len(s) - 2, - 1, -1):
            right_min[back] = smallest
            smallest = min(smallest , (s[back], back))

        
        min_char_at = s.index(min(s))
        result_seq = []
        for i in range(min_char_at + 1):
            stack.append((s[i], i))

        while stack:
            min_ind = stack[-1][1]
            smallest_far = right_min[min_ind]
            
            while stack and stack[-1][0] <= smallest_far[0]:
                result_seq.append(stack.pop())

            next_dest = smallest_far[1]
            for i in range(min_ind + 1, min(next_dest + 1 , len(s))):
                stack.append((s[i], i))
        

        
        return "".join([tup[0] for tup in result_seq])
