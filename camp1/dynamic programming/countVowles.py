class Solution:
    def countVowels(self, word: str) -> int:
        length_dict = defaultdict(int)
        word_len = len(word)
        vowels_set = {'a' , 'e' , 'i', 'o','u'}
        for index , char in enumerate(word):
            length_dict[char] += (index * (word_len - index))
            length_dict[char] += (word_len - index) 

        output = 0
        for ch in length_dict:
            if ch in vowels_set: output += length_dict[ch]
                
        return output