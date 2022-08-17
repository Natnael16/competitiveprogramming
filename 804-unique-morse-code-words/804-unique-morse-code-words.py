class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        low_start = 97
        end = 97 + 26
        encode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        word_di = {}
        j = 0
        for i in range(low_start , end):
            word_di[chr(i)] = j
            j += 1
        different_t = set()
        
        for word in words:
            w_code = ""
            for char in word:
                w_code+=encode[word_di[char]]
            different_t.add(w_code)
        return len(different_t)
            
        