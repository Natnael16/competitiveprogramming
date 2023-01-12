#User function Template for python3
from collections import defaultdict, deque
class Solution:
    def buildGraph(self,dictionary,indegree):
        graph = defaultdict(list)
        prev = ""
        for word in dictionary:
            if prev and prev[0] != word[0]:
                graph[prev[0]].append(word[0])
                indegree[word[0]] += 1
            else:
                left , right = 1 , 1
                while left < len(prev) and right < len(word):
                    if prev[left] != word[right]:
                        graph[prev[left]].append(word[right])
                        indegree[word[right]] += 1
                        break
                    
                    left += 1 ; right += 1
            prev = word
        return graph
        
    
    def findOrder(self,dictionary, N, K):
        indegree = defaultdict(int)
        words_set = set([char for word in dictionary for char in word ])
        graph = self.buildGraph(dictionary,indegree)
        queue = deque()
        for char in words_set:
            if indegree[char] == 0:
                queue.append(char)
        
        seq = []
        while queue:
            cur_char = queue.popleft()
            seq.append(cur_char)
            for neigh in graph[cur_char]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        # print(seq)
        return seq
        
        
        
        
    # code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends