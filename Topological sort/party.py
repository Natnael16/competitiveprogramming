from collections import defaultdict, deque


nodes = int(input())

employee_map = defaultdict(list)
for node in range(1 , nodes + 1):
    employee_map[int(input())].append(node)

q = deque()
q.extend(employee_map[-1])
level = 1
while q:
    for i in range(len(q)):
        cur = q.popleft()
        q.extend(employee_map[cur])
    if q:
        level += 1
print(level)

