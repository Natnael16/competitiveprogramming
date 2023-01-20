class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        set1 , set2 = Counter(word1), Counter(word2)
        count_one , count_two = len(set1), len(set2)
        for word in set1:
            for word2 in set2:
                change1 , change2 = False , False
                # remove
                if set1[word] == 1:
                    count_one -= 1
                    set1[word] -= 1
                    change1 = True
                if set2[word2] == 1:
                    count_two -= 1
                    set2[word2] -= 1
                    change2 = True
                # add
                if set1[word2] == 0:
                    count_one += 1
        
                if set2[word] == 0:
                    count_two += 1
                
                #check
                if count_one == count_two:
                    return True

                #reset
                if change1:
                    set1[word] += 1
                if change2:
                    set2[word2] += 1
                count_one , count_two = len(set1), len(set2)
        return False
                 

        

            
            

