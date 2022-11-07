class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        words_count = Counter(words)
        pal_count = 0
        odds = 0
        for word in words:
            if words_count[word] > 0:
                reverse = word[::-1]
                if word == reverse:
                    if not words_count[word] % 2:
                        pal_count += words_count[word] * 2
                        words_count[word] = 0
                    else:
                        pal_count += (words_count[word] - 1) * 2
                        odds += 1
                        words_count[word] = 0
                
                elif words_count[reverse] > 0:
                    words_count[word] -= 1
                    pal_count += 4
                    words_count[reverse] -= 1
       
        return pal_count + 2 if odds else pal_count
            
            
            
        
        