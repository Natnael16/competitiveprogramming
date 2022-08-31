class Solution:
def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
p_set = set()
a_set = set()
q1 = deque([])
q2 = deque([])
dirs = [0,-1,0,1,0]
inbound = lambda row, col : 0 <= row < len(heights) and 0 <= col < len(heights[0])
for col in range(len(heights[0])):
p_set.add((0 , col))
q1.append((0 , col))
for row in range(len(heights)):
p_set.add((row , 0))
q1.append((row , 0))
for col in range(len(heights[0])):
a_set.add((len(heights) - 1 , col))
q1.append((len(heights) - 1 , col))
for row in range(len(heights)):
a_set.add((row , len(heights[0]) - 1))
q1.append((row , len(heights[0]) - 1))
def bfs(queue, set_ , dirs ):
while queue:
r , c = queue.popleft()
for i in range(4):
new_r , new_c = r + dirs[i] , c + dirs[i + 1]
if inbound(new_r , new_c) and heights[new_r][new_c] not in set_ and  heights[new_r][new_c] >= heights[r][c]:
queue.append((new_r , new_c))
set_.add((new_r , new_c))
bfs(q1, p_set, dirs )
bfs(q2 ,a_set , dirs)
res= []
for row in range(len(heights)):
for col in range(len(heights[0])):
if (row, col ) in p_set and (row, col) in a_set:
res.append((row, col))
return res