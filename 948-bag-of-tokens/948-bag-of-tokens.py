class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        '''
        sort them by tokens
        take minimum one as far as you can 
            record the answer so far
        else
        face down and continue
        '''
        s_tokens = sorted(tokens)
        
        i , j = 0, len(tokens) - 1
        ans = 0
        count = 0
        while i <= j:
            if power - s_tokens[i] >= 0:
                power -= s_tokens[i]
                count += 1
                i += 1
                
            elif count > 0:
                power += s_tokens[j]
                j -= 1
                count -= 1
            else:
                break
                
            ans = max(ans, count)
        return ans
                