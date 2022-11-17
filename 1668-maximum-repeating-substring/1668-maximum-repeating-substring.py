class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        left = 0 
        window_size = len(word)
        max_k = 0
        count = 0
        right = window_size - 1
        while right < len(sequence):
            temp_left , temp_right = left, right
            while temp_right < len(sequence) and sequence[temp_left:temp_right + 1] == word:
                count += 1
                max_k = max(max_k, count)
                temp_left += window_size
                temp_right += window_size
            else:
                count = 0
                right += 1
                left += 1
            
        return max_k
            
            