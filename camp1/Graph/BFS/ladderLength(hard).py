class Solution:

    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        adj_list = {}
        wordList.append(beginWord)
        for word in wordList:
            for char in range(len(word)):
                temp = word[:char] + '_' + word[char + 1:]
                # temp = word.replace(char,'')
                if temp in adj_list:
                    adj_list[temp].append(word)
                else:
                    adj_list[temp] = [word]
        # print(adj_list)
        q = deque([beginWord])
        steps = 1
        visited = set()
        visited.add(beginWord)
        while q:

            for i in range(len(q)):

                cur_word = q.popleft()
                if cur_word == endWord:
                    return steps
                visited.add(cur_word)
                for ch in range(len(cur_word)):
                    temp = cur_word[:ch] + '_' + cur_word[ch + 1:]
                    adj_words = adj_list[temp]
                    for w in adj_words:
                        if w not in visited:
                            q.append(w)
            steps += 1
        return 0